import numpy as np
import torch
from mmpose.models import builder
from mmpose.models.builder import POSENETS
from mmpose.models.detectors.base import BasePose
from transformers import BertTokenizerFast

from models.models.backbones.swin_utils import load_pretrained
import os
import clip
# import open_clip
# from sentence_transformers import SentenceTransformer
from transformers import AutoModel, AutoTokenizer
from transformers import BertTokenizer, BertModel
import random

@POSENETS.register_module()
class PoseAnythingModel(BasePose):
    """Few-shot keypoint detectors.
    Args:
        keypoint_head (dict): Keypoint head to process feature.
        encoder_config (dict): Config for encoder. Default: None.
        pretrained (str): Path to the pretrained image models.
        text_pretrained (str): Path to the pretrained text models.
        train_cfg (dict): Config for training. Default: None.
        test_cfg (dict): Config for testing. Default: None.
    """

    def __init__(self,
                 keypoint_head,
                 encoder_config,
                 pretrained=False,
                 text_pretrained=False,
                 finetune_text_pretrained=False,
                 train_cfg=None,
                 test_cfg=None):
        super().__init__()
        self.backbone, self.backbone_type = self.init_backbone(pretrained, encoder_config)
        self.finetune_text_pretrained = finetune_text_pretrained
        self.text_backbone, self.tokenizer, self.text_backbone_type = self.init_text_backbone(text_pretrained)
        self.keypoint_head = builder.build_head(keypoint_head)
        self.keypoint_head.init_weights()
        self.train_cfg = train_cfg
        self.test_cfg = test_cfg
        self.target_type = test_cfg.get('target_type',
                                        'GaussianHeatMap')  # GaussianHeatMap


    def init_text_backbone(self, text_pretrained):
        if "ViT" in text_pretrained:
            text_backbone, _ = clip.load(
                text_pretrained,
                download_root=os.getenv('TORCH_HOME', os.path.join(os.path.expanduser('~'), '.cache', 'torch')),
                jit=False)
            tokenizer = clip.tokenize
            text_backbone_type = "clip"

            # Freeze all parameters of the visual backbone
            for param in text_backbone.visual.parameters():
                param.requires_grad = False

        elif "gte" in text_pretrained:
            tokenizer = AutoTokenizer.from_pretrained(text_pretrained)
            text_backbone = AutoModel.from_pretrained(text_pretrained, trust_remote_code=True)
            text_backbone_type = "gte"

        elif "bert-base-multilingual" in text_pretrained:
            tokenizer = BertTokenizer.from_pretrained(text_pretrained)
            text_backbone = BertModel.from_pretrained(text_pretrained)
            text_backbone_type = "bert-multilingual"

        self.text_backbone_device = "cuda" if torch.cuda.is_available() else "cpu"
        text_backbone.to(device=self.text_backbone_device)

        if self.finetune_text_pretrained:
            if text_backbone_type == "clip":
                # https://github.com/openai/CLIP/issues/57
                for p in text_backbone.parameters():
                    p.data = p.data.float()
            text_backbone.train()
        else:
            text_backbone.eval()

        return text_backbone, tokenizer, text_backbone_type


    def init_backbone(self, pretrained, encoder_config):
        if 'swin' in pretrained:
            encoder_sample = builder.build_backbone(encoder_config)
            if '.pth' in pretrained:
                load_pretrained(pretrained, encoder_sample, logger=None)
            backbone = 'swin'
        elif 'dino' in pretrained:
            if 'dinov2' in pretrained:
                repo = 'facebookresearch/dinov2'
                backbone = 'dinov2'
            else:
                repo = 'facebookresearch/dino:main'
                backbone = 'dino'
            encoder_sample = torch.hub.load(repo, pretrained)
        elif 'resnet' in pretrained:
            pretrained = 'torchvision://resnet50'
            encoder_config = dict(type='ResNet', depth=50, out_indices=(3,))
            encoder_sample = builder.build_backbone(encoder_config)
            encoder_sample.init_weights(pretrained)
            backbone = 'resnet50'
        else:
            raise NotImplementedError(f'backbone {pretrained} not supported')
        return encoder_sample, backbone

    @property
    def with_keypoint(self):
        """Check if has keypoint_head."""
        return hasattr(self, 'keypoint_head')

    def init_weights(self, pretrained=None):
        """Weight initialization for model."""
        self.backbone.init_weights(pretrained)
        self.encoder_query.init_weights(pretrained)
        self.keypoint_head.init_weights()

    def forward(self,
                img_s,
                img_q,
                target_s=None,
                target_weight_s=None,
                target_q=None,
                target_weight_q=None,
                img_metas=None,
                return_loss=True,
                **kwargs):
        """Defines the computation performed at every call."""

        if return_loss:
            return self.forward_train(img_s, target_s, target_weight_s, img_q,
                                      target_q, target_weight_q, img_metas,
                                      **kwargs)
        else:
            return self.forward_test(img_s, target_s, target_weight_s, img_q,
                                     target_q, target_weight_q, img_metas,
                                     **kwargs)

    def forward_dummy(self, img_s, target_s, target_weight_s, img_q, target_q,
                      target_weight_q, img_metas, **kwargs):
        return self.predict(
            img_s, target_s, target_weight_s, img_q, img_metas)

    def forward_train(self,
                      img_s,
                      target_s,
                      target_weight_s,
                      img_q,
                      target_q,
                      target_weight_q,
                      img_metas,
                      **kwargs):

        """Defines the computation performed at every call when training."""
        bs, _, h, w = img_q.shape

        output, initial_proposals, similarity_map, mask_s = self.predict(
            img_s, target_s, target_weight_s, img_q, img_metas)

        # parse the img meta to get the target keypoints
        target_keypoints = self.parse_keypoints_from_img_meta(img_metas, output.device, keyword='query')
        target_sizes = torch.tensor([img_q.shape[-2], img_q.shape[-1]]).unsqueeze(0).repeat(img_q.shape[0], 1, 1)

        # if return loss
        losses = dict()
        if self.with_keypoint:
            keypoint_losses = self.keypoint_head.get_loss(
                output, initial_proposals, similarity_map, target_keypoints,
                target_q, target_weight_q * mask_s, target_sizes)
            losses.update(keypoint_losses)
            keypoint_accuracy = self.keypoint_head.get_accuracy(output[-1],
                                                                target_keypoints,
                                                                target_weight_q * mask_s,
                                                                target_sizes,
                                                                height=h)
            losses.update(keypoint_accuracy)

        return losses

    def forward_test(self,
                     img_s,
                     target_s,
                     target_weight_s,
                     img_q,
                     target_q,
                     target_weight_q,
                     img_metas=None,
                     **kwargs):

        """Defines the computation performed at every call when testing."""
        batch_size, _, img_height, img_width = img_q.shape

        # # masking the query image
        # patch_size = 128
        # patch_location = (
        #     random.randint(0, img_height - patch_size),
        #     random.randint(0, img_width - patch_size))
        # mask = torch.ones_like(img_q)
        # mask[:, :, patch_location[0]:patch_location[0] + patch_size,
        # patch_location[1]:patch_location[1] + patch_size] = 0
        # # img_s[0] = img_s[0] * mask
        # img_q = img_q * mask

        output, initial_proposals, similarity_map, _ = self.predict(img_s, target_s, target_weight_s, img_q, img_metas)
        predicted_pose = output[-1].detach().cpu().numpy()  # [bs, num_query, 2]

        result = {}
        if self.with_keypoint:
            keypoint_result = self.keypoint_head.decode(img_metas, predicted_pose, img_size=[img_width, img_height])
            result.update(keypoint_result)

        result.update({
            "points":
                torch.cat((initial_proposals, output.squeeze(1))).cpu().numpy()
        })
        result.update({"sample_image_file": img_metas[0]['sample_image_file']})

        return result

    def predict(self,
                img_s,
                target_s,
                target_weight_s,
                img_q,
                img_metas=None):

        batch_size, _, img_height, img_width = img_q.shape
        mask_s = target_weight_s[0]
        max_points = mask_s.shape[1]
        assert [i['sample_skeleton'][0] != i['query_skeleton'] for i in img_metas]
        skeleton = [i['sample_skeleton'][0] for i in img_metas]

        all_shots_point_descriptions = self.extract_text_features(img_metas, max_points, mask_s)
        feature_q, feature_s = self.extract_image_features(img_s, img_q)

        output, initial_proposals, similarity_map = self.keypoint_head(feature_q, feature_s, target_s, mask_s,
                                                                       skeleton, all_shots_point_descriptions)
        return output, initial_proposals, similarity_map, mask_s

    def extract_image_features(self, img_s, img_q):
        if self.backbone_type == 'swin':
            feature_q = self.backbone.forward_features(img_q)  # [bs, C, h, w]
            # feature_s = [self.backbone.forward_features(img) for img in img_s]
            feature_s = None
        elif self.backbone_type == 'dino':
            batch_size, _, img_height, img_width = img_q.shape
            feature_q = self.backbone.get_intermediate_layers(img_q, n=1)[0][:, 1:] \
                .reshape(batch_size, img_height // 8, img_width // 8, -1).permute(0, 3, 1, 2)  # [bs, 3, h, w]
            feature_s = [self.backbone.get_intermediate_layers(img, n=1)[0][:, 1:].
                         reshape(batch_size, img_height // 8, img_width // 8, -1).permute(0, 3, 1, 2) for img in img_s]
        elif self.backbone_type == 'dinov2':
            batch_size, _, img_height, img_width = img_q.shape
            feature_q = self.backbone.get_intermediate_layers(img_q, n=1, reshape=True)[0]  # [bs, c, h, w]
            feature_s = [self.backbone.get_intermediate_layers(img, n=1, reshape=True)[0] for img in img_s]
        elif self.backbone_type == 'clip':
            with torch.no_grad():
                feature_q = self.backbone.model(img_q)
                feature_s = None
        else:
            feature_s = [self.backbone(img) for img in img_s]
            feature_q = self.encoder_query(img_q)

        return feature_q, feature_s


    def extract_text_features(self, img_metas, max_points, mask_s):
        with torch.set_grad_enabled(self.finetune_text_pretrained):
            all_shots_point_descriptions = []
            for shot in range(len(img_metas[0]['sample_point_descriptions'])):
                support_descriptions = [i['sample_point_descriptions'][shot] for i in img_metas]

                # ignore non-visible points
                # support_descriptions = [description[mask[:len(description)].view(-1) == 1] for mask, description in zip(mask_s.cpu(), support_descriptions)]
                support_descriptions = [description[list(mask[:len(description)].view(-1) == 1)] for mask, description in
                                        zip(mask_s.cpu(), support_descriptions)]

                all_points = [point for description in support_descriptions for point in description]
                # # CLIP
                if self.text_backbone_type == "clip":
                    tokens = self.tokenizer(all_points).to(device=self.text_backbone_device)
                    all_descriptions = self.text_backbone.encode_text(tokens)
                    all_descriptions = all_descriptions / all_descriptions.norm(dim=1, keepdim=True).to(dtype=torch.float32)

                # TRANSFORMERS
                elif self.text_backbone_type == "gte" or self.text_backbone_type == "bert-multilingual":
                    tokens = self.tokenizer(all_points, max_length=77, padding=True, truncation=True, return_tensors='pt').to(device=self.text_backbone_device)
                    all_descriptions = self.text_backbone(**tokens)
                    all_descriptions = all_descriptions.last_hidden_state[:, 0]
                    all_descriptions = torch.nn.functional.normalize(all_descriptions, p=2, dim=1)

                # Divide it back into a list of lists with original lengths
                batch_padded_tensors = []
                start_index = 0
                for i, description in enumerate(support_descriptions):
                    end_index = start_index + len(description)
                    # # pad all unused points with 0, up to max_points (default is 100)
                    padded_tensor = torch.zeros(max_points, all_descriptions.shape[-1]).to(device=self.text_backbone_device).detach()
                    padded_tensor[mask_s[i].view(-1) == 1] = all_descriptions[start_index:end_index]

                    batch_padded_tensors.append(padded_tensor)
                    start_index = end_index
                all_shots_point_descriptions.append(torch.stack(batch_padded_tensors, dim=0))

            return torch.mean(torch.stack(all_shots_point_descriptions, dim=0), 0)

    def parse_keypoints_from_img_meta(self, img_meta, device, keyword='query'):
        """Parse keypoints from the img_meta.

        Args:
            img_meta (dict): Image meta info.
            device (torch.device): Device of the output keypoints.
            keyword (str): 'query' or 'sample'. Default: 'query'.

        Returns:
            Tensor: Keypoints coordinates of query images.
        """

        if keyword == 'query':
            query_kpt = torch.stack([
                torch.tensor(info[f'{keyword}_joints_3d']).to(device)
                for info in img_meta
            ], dim=0)[:, :, :2]  # [bs, num_query, 2]
        else:
            query_kpt = []
            for info in img_meta:
                if isinstance(info[f'{keyword}_joints_3d'][0], torch.Tensor):
                    samples = torch.stack(info[f'{keyword}_joints_3d'])
                else:
                    samples = np.array(info[f'{keyword}_joints_3d'])
                query_kpt.append(torch.tensor(samples).to(device)[:, :, :2])
            query_kpt = torch.stack(query_kpt, dim=0)  # [bs, , num_samples, num_query, 2]
        return query_kpt


    # UNMODIFIED
    def show_result(self,
                    img,
                    result,
                    skeleton=None,
                    kpt_score_thr=0.3,
                    bbox_color='green',
                    pose_kpt_color=None,
                    pose_limb_color=None,
                    radius=4,
                    text_color=(255, 0, 0),
                    thickness=1,
                    font_scale=0.5,
                    win_name='',
                    show=False,
                    wait_time=0,
                    out_file=None):
        """Draw `result` over `img`.

        Args:
            img (str or Tensor): The image to be displayed.
            result (list[dict]): The results to draw over `img`
                (bbox_result, pose_result).
            kpt_score_thr (float, optional): Minimum score of keypoints
                to be shown. Default: 0.3.
            bbox_color (str or tuple or :obj:`Color`): Color of bbox lines.
            pose_kpt_color (np.array[Nx3]`): Color of N keypoints.
                If None, do not draw keypoints.
            pose_limb_color (np.array[Mx3]): Color of M limbs.
                If None, do not draw limbs.
            text_color (str or tuple or :obj:`Color`): Color of texts.
            thickness (int): Thickness of lines.
            font_scale (float): Font scales of texts.
            win_name (str): The window name.
            wait_time (int): Value of waitKey param.
                Default: 0.
            out_file (str or None): The filename to write the image.
                Default: None.

        Returns:
            Tensor: Visualized img, only if not `show` or `out_file`.
        """

        img = mmcv.imread(img)
        img = img.copy()
        img_h, img_w, _ = img.shape

        bbox_result = []
        pose_result = []
        for res in result:
            bbox_result.append(res['bbox'])
            pose_result.append(res['keypoints'])

        if len(bbox_result) > 0:
            bboxes = np.vstack(bbox_result)
            # draw bounding boxes
            mmcv.imshow_bboxes(
                img,
                bboxes,
                colors=bbox_color,
                top_k=-1,
                thickness=thickness,
                show=False,
                win_name=win_name,
                wait_time=wait_time,
                out_file=None)

            for person_id, kpts in enumerate(pose_result):
                # draw each point on image
                if pose_kpt_color is not None:
                    assert len(pose_kpt_color) == len(kpts), (
                        len(pose_kpt_color), len(kpts))
                    for kid, kpt in enumerate(kpts):
                        x_coord, y_coord, kpt_score = int(kpt[0]), int(
                            kpt[1]), kpt[2]
                        if kpt_score > kpt_score_thr:
                            img_copy = img.copy()
                            r, g, b = pose_kpt_color[kid]
                            cv2.circle(img_copy, (int(x_coord), int(y_coord)),
                                       radius, (int(r), int(g), int(b)), -1)
                            transparency = max(0, min(1, kpt_score))
                            cv2.addWeighted(
                                img_copy,
                                transparency,
                                img,
                                1 - transparency,
                                0,
                                dst=img)

                # draw limbs
                if skeleton is not None and pose_limb_color is not None:
                    assert len(pose_limb_color) == len(skeleton)
                    for sk_id, sk in enumerate(skeleton):
                        pos1 = (int(kpts[sk[0] - 1, 0]), int(kpts[sk[0] - 1,
                        1]))
                        pos2 = (int(kpts[sk[1] - 1, 0]), int(kpts[sk[1] - 1,
                        1]))
                        if (pos1[0] > 0 and pos1[0] < img_w and pos1[1] > 0
                                and pos1[1] < img_h and pos2[0] > 0
                                and pos2[0] < img_w and pos2[1] > 0
                                and pos2[1] < img_h
                                and kpts[sk[0] - 1, 2] > kpt_score_thr
                                and kpts[sk[1] - 1, 2] > kpt_score_thr):
                            img_copy = img.copy()
                            X = (pos1[0], pos2[0])
                            Y = (pos1[1], pos2[1])
                            mX = np.mean(X)
                            mY = np.mean(Y)
                            length = ((Y[0] - Y[1]) ** 2 + (X[0] - X[1]) ** 2) ** 0.5
                            angle = math.degrees(
                                math.atan2(Y[0] - Y[1], X[0] - X[1]))
                            stickwidth = 2
                            polygon = cv2.ellipse2Poly(
                                (int(mX), int(mY)),
                                (int(length / 2), int(stickwidth)), int(angle),
                                0, 360, 1)

                            r, g, b = pose_limb_color[sk_id]
                            cv2.fillConvexPoly(img_copy, polygon,
                                               (int(r), int(g), int(b)))
                            transparency = max(
                                0,
                                min(
                                    1, 0.5 *
                                       (kpts[sk[0] - 1, 2] + kpts[sk[1] - 1, 2])))
                            cv2.addWeighted(
                                img_copy,
                                transparency,
                                img,
                                1 - transparency,
                                0,
                                dst=img)

        show, wait_time = 1, 1
        if show:
            height, width = img.shape[:2]
            max_ = max(height, width)

            factor = min(1, 800 / max_)
            enlarge = cv2.resize(
                img, (0, 0),
                fx=factor,
                fy=factor,
                interpolation=cv2.INTER_CUBIC)
            imshow(enlarge, win_name, wait_time)

        if out_file is not None:
            imwrite(img, out_file)

        return img
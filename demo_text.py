import argparse
import copy
import os
import pickle
import random
import cv2
import numpy as np
import string
import torch
from mmcv import Config, DictAction
from mmcv.cnn import fuse_conv_bn
from mmcv.runner import load_checkpoint
from mmpose.core import wrap_fp16_model
from mmpose.models import build_posenet
from torchvision import transforms
from models import *
import torchvision.transforms.functional as F

from tools.visualization import plot_results, plot_query_results, plot_modified_query
import ast
import shutil

COLORS = [
    [255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0],
    [85, 255, 0], [0, 255, 0], [0, 255, 85], [0, 255, 170], [0, 255, 255],
    [0, 170, 255], [0, 85, 255], [0, 0, 255], [85, 0, 255], [170, 0, 255],
    [255, 0, 255], [255, 0, 170], [255, 0, 85], [255, 0, 0]]

class Resize_Pad:
    def __init__(self, w=256, h=256):
        self.w = w
        self.h = h

    def __call__(self, image):
        _, w_1, h_1 = image.shape
        ratio_1 = w_1 / h_1
        # check if the original and final aspect ratios are the same within a margin
        if round(ratio_1, 2) != 1:
            # padding to preserve aspect ratio
            if ratio_1 > 1:  # Make the image higher
                hp = int(w_1 - h_1)
                hp = hp // 2
                image = F.pad(image, (hp, 0, hp, 0), 0, "constant")
                return F.resize(image, [self.h, self.w])
            else:
                wp = int(h_1 - w_1)
                wp = wp // 2
                image = F.pad(image, (0, wp, 0, wp), 0, "constant")
                return F.resize(image, [self.h, self.w])
        else:
            return F.resize(image, [self.h, self.w])


def transform_keypoints_to_pad_and_resize(keypoints, image_size):
    trans_keypoints = keypoints.clone()
    h, w = image_size[:2]
    ratio_1 = w / h
    if ratio_1 > 1:
        # width is bigger than height - pad height
        hp = int(w - h)
        hp = hp // 2
        trans_keypoints[:, 1] = keypoints[:, 1] + hp
        trans_keypoints *= (256. / w)
    else:
        # height is bigger than width - pad width
        wp = int(image_size[1] - image_size[0])
        wp = wp // 2
        trans_keypoints[:, 0] = keypoints[:, 0] + wp
        trans_keypoints *= (256. / h)
    return trans_keypoints


def parse_args():
    parser = argparse.ArgumentParser(description='Pose Anything Demo')
    parser.add_argument('--support_points', help='support keypoints text descriptions')
    parser.add_argument('--support_skeleton', help='list of keypoints skeleton')
    parser.add_argument('--query', help='Image file')
    parser.add_argument('--config', default=None, help='test config file path')
    parser.add_argument('--checkpoint', default=None, help='checkpoint file')
    parser.add_argument('--outdir', default='output', help='checkpoint file')

    parser.add_argument(
        '--fuse-conv-bn',
        action='store_true',
        help='Whether to fuse conv and bn, this will slightly increase'
             'the inference speed')
    parser.add_argument(
        '--cfg-options',
        nargs='+',
        action=DictAction,
        default={},
        help='override some settings in the used config, the key-value pair '
             'in xxx=yyy format will be merged into config file. For example, '
             "'--cfg-options model.backbone.depth=18 model.backbone.with_cp=True'")
    args = parser.parse_args()
    return args


def merge_configs(cfg1, cfg2):
    # Merge cfg2 into cfg1
    # Overwrite cfg1 if repeated, ignore if value is None.
    cfg1 = {} if cfg1 is None else cfg1.copy()
    cfg2 = {} if cfg2 is None else cfg2
    for k, v in cfg2.items():
        if v:
            cfg1[k] = v
    return cfg1


def main():
    random.seed(0)
    np.random.seed(0)
    torch.manual_seed(0)

    args = parse_args()
    cfg = Config.fromfile(args.config)

    if args.cfg_options is not None:
        cfg.merge_from_dict(args.cfg_options)
    # set cudnn_benchmark
    if cfg.get('cudnn_benchmark', False):
        torch.backends.cudnn.benchmark = True
    cfg.data.test.test_mode = True

    os.makedirs(args.outdir, exist_ok=True)

    # Load data
    point_descriptions = ast.literal_eval(args.support_points)
    query_img = cv2.imread(args.query)
    if query_img is None:
        raise ValueError('Fail to read image')

    # just a placeholder, we don't have input keypoints
    kp_src = torch.zeros((len(point_descriptions), 2))

    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
        Resize_Pad(cfg.model.encoder_config.img_size, cfg.model.encoder_config.img_size)])

    if args.support_skeleton is not None:
        skeleton = ast.literal_eval(args.support_skeleton)
    if len(skeleton) == 0:
        skeleton = [(0, 0)]

    model_device = "cuda" if torch.cuda.is_available() else "cpu"

    query_img = preprocess(query_img).flip(0)[None].to(model_device)
    # Create heatmap from keypoints
    genHeatMap = TopDownGenerateTargetFewShot()
    data_cfg = cfg.data_cfg
    data_cfg['image_size'] = np.array([cfg.model.encoder_config.img_size, cfg.model.encoder_config.img_size])
    data_cfg['joint_weights'] = None
    data_cfg['use_different_joint_weights'] = False
    kp_src_3d = torch.concatenate((kp_src, torch.zeros(kp_src.shape[0], 1)), dim=-1)
    kp_src_3d_weight = torch.concatenate((torch.ones_like(kp_src), torch.zeros(kp_src.shape[0], 1)), dim=-1)

    # everything that is related to the support image is used as placeholder
    target_s, target_weight_s = genHeatMap._msra_generate_target(data_cfg, kp_src_3d, kp_src_3d_weight, sigma=1)
    target_s = torch.tensor(target_s).float()[None]
    target_weight_s = torch.tensor(target_weight_s).float()[None].to(model_device)

    data = {
        'img_s': [0],
        'img_q': query_img,
        'target_s': [target_s],
        'target_weight_s': [target_weight_s],
        'target_q': None,
        'target_weight_q': None,
        'return_loss': False,
        'img_metas': [{'sample_skeleton': [skeleton],
                       'query_skeleton': skeleton,
                       'sample_point_descriptions': np.array([point_descriptions]),
                       'sample_joints_3d': [kp_src_3d],
                       'query_joints_3d': kp_src_3d,
                       'sample_center': [kp_src.mean(dim=0)],
                       'query_center': kp_src.mean(dim=0),
                       'sample_scale': [kp_src.max(dim=0)[0] - kp_src.min(dim=0)[0]],
                       'query_scale': kp_src.max(dim=0)[0] - kp_src.min(dim=0)[0],
                       'sample_rotation': [0],
                       'query_rotation': 0,
                       'sample_bbox_score': [1],
                       'query_bbox_score': 1,
                       'query_image_file': '',
                       'sample_image_file': [''],
                       }]
    }

    # Load model
    model = build_posenet(cfg.model)
    fp16_cfg = cfg.get('fp16', None)
    if fp16_cfg is not None:
        wrap_fp16_model(model)
    load_checkpoint(model, args.checkpoint, map_location='cpu')
    if args.fuse_conv_bn:
        model = fuse_conv_bn(model)
    model.to(model_device)
    model.eval()

    with torch.no_grad():
        outputs = model(**data)

    # visualize results
    vis_q_weight = target_weight_s[0]
    vis_q_image = query_img[0].detach().cpu().numpy().transpose(1, 2, 0)

    name_idx = plot_query_results(vis_q_image, vis_q_weight, skeleton, torch.tensor(outputs['points']).squeeze(0), out_dir=args.outdir)
    shutil.copyfile(args.query, f'./{args.outdir}/{str(name_idx)}_query_in.png')


if __name__ == '__main__':
    main()

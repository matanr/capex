import argparse
import random

import gradio as gr
import matplotlib
import numpy as np
import torch
from PIL import ImageDraw, Image
from matplotlib import pyplot as plt
from mmcv import Config
from mmcv.runner import load_checkpoint
from mmpose.core import wrap_fp16_model
from mmpose.models import build_posenet
from torchvision import transforms

from demo_text import Resize_Pad
from models import *

import networkx as nx
import matplotlib.pyplot as plt
import ast
import cv2

def edges_prompt_to_list(prompt):
    if prompt[0] != "[":
        prompt = "[" + prompt
    if prompt[-1] != "]":
        prompt += "]"
    return ast.literal_eval(prompt)

def descriptions_prompt_to_list(prompt):
    return prompt.split(',')


# Function to visualize the graph
def visualize_graph(node_descriptions, edges, state):
    node_descriptions = descriptions_prompt_to_list(node_descriptions)
    edges = edges_prompt_to_list(edges)
    state['point_descriptions'] = node_descriptions
    state['skeleton'] = edges

    # Create an empty graph
    G = nx.Graph()
    G.clear()

    # Add nodes with descriptions
    for i, desc in enumerate(node_descriptions):
        G.add_node(i, label=f'{i}:{desc}')

    # Add edges
    for edge in edges:
        G.add_edge(edge[0], edge[1])

    # Draw the graph
    pos = nx.spring_layout(G)  # Define layout
    labels = nx.get_node_attributes(G, 'label')  # Get labels
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=1500, node_color='skyblue', font_size=10, font_weight='bold', font_color='black')  # Draw nodes with labels
    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')  # Draw edges
    plt.title("Graph Visualization")  # Set title
    plt.axis('off')  # Turn off axis
    # plt.show()  # Show plot
    # Image from plot
    fig = plt.gcf()
    # fig.tight_layout(pad=0)

    # To remove the huge white borders
    # plt.margins(0)

    fig.canvas.draw()
    image_from_plot = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    image_from_plot = image_from_plot.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.clf()
    return image_from_plot, state

# Copyright (c) OpenMMLab. All rights reserved.
# os.system('python -m pip install timm')
# os.system('python -m pip install Openmim')
# os.system('python -m mim install mmengine')
# os.system('python -m mim install "mmcv-full==1.6.2"')
# os.system('python -m mim install "mmpose==0.29.0"')
# os.system('python -m mim install "gradio==3.44.0"')
# os.system('python setup.py develop')

matplotlib.use('agg')
checkpoint_path = ''



def plot_query_results(query_img, query_w, skeleton, prediction, radius=6):
    h, w, c = query_img.shape
    prediction = prediction[-1].cpu().numpy() * h
    query_img = (query_img - np.min(query_img)) / (
            np.max(query_img) - np.min(query_img))
    for id, (img, w, keypoint) in enumerate(zip([query_img],
                                                [query_w],
                                                [prediction])):
        f, axes = plt.subplots()
        plt.imshow(img)
        for k in range(keypoint.shape[0]):
            if w[k] > 0:
                kp = keypoint[k, :2]
                c = (1, 0, 0, 0.75) if w[k] == 1 else (0, 0, 1, 0.6)
                patch = plt.Circle(kp, radius, color=c)
                axes.add_patch(patch)
                axes.text(kp[0], kp[1], k)
                plt.draw()
        for l, limb in enumerate(skeleton):
            kp = keypoint[:, :2]
            if l > len(COLORS) - 1:
                c = [x / 255 for x in random.sample(range(0, 255), 3)]
            else:
                c = [x / 255 for x in COLORS[l]]
            if w[limb[0]] > 0 and w[limb[1]] > 0:
                patch = plt.Line2D([kp[limb[0], 0], kp[limb[1], 0]],
                                   [kp[limb[0], 1], kp[limb[1], 1]],
                                   linewidth=6, color=c, alpha=0.6)
                axes.add_artist(patch)
        plt.axis('off')  # command for hiding the axis.
        plt.subplots_adjust(0, 0, 1, 1, 0, 0)
        plt.margins(0)
        fig = plt.gcf()
        fig.tight_layout(pad=0)

        return plt

COLORS = [
    [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0],
    [85, 255, 0], [0, 255, 0], [0, 255, 85], [0, 255, 170], [0, 255, 255],
    [0, 170, 255], [0, 85, 255], [0, 0, 255], [85, 0, 255], [170, 0, 255],
    [255, 0, 255], [255, 0, 170], [255, 0, 85], [255, 0, 0]
]


def process(query_img, node_descriptions, edges, state,
            cfg_path='configs/1shot-swin-gte/graph_split1_config.py'):
    node_descriptions = descriptions_prompt_to_list(node_descriptions)
    edges = edges_prompt_to_list(edges)
    state['point_descriptions'] = node_descriptions
    state['skeleton'] = edges
    cfg = Config.fromfile(cfg_path)
    kp_src_tensor = torch.zeros((len(state['point_descriptions']), 2))
    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
        Resize_Pad(cfg.model.encoder_config.img_size,
                   cfg.model.encoder_config.img_size)])

    if len(state['skeleton']) == 0:
        state['skeleton'] = [(0, 0)]

    model_device = "cuda" if torch.cuda.is_available() else "cpu"

    np_query = np.array(query_img)[:, :, ::-1].copy()
    q_img = preprocess(np_query).flip(0)[None].to(model_device)
    # Create heatmap from keypoints
    genHeatMap = TopDownGenerateTargetFewShot()
    data_cfg = cfg.data_cfg
    data_cfg['image_size'] = np.array([cfg.model.encoder_config.img_size,
                                       cfg.model.encoder_config.img_size])
    data_cfg['joint_weights'] = None
    data_cfg['use_different_joint_weights'] = False
    kp_src_3d = torch.cat(
        (kp_src_tensor, torch.zeros(kp_src_tensor.shape[0], 1)), dim=-1)
    kp_src_3d_weight = torch.cat(
        (torch.ones_like(kp_src_tensor),
         torch.zeros(kp_src_tensor.shape[0], 1)), dim=-1)
    target_s, target_weight_s = genHeatMap._msra_generate_target(data_cfg,
                                                                 kp_src_3d,
                                                                 kp_src_3d_weight,
                                                                 sigma=1)
    target_s = torch.tensor(target_s).float()[None]
    target_weight_s = torch.ones_like(
        torch.tensor(target_weight_s).float()[None]).to(model_device)

    data = {
        'img_s': [0],
        'img_q': q_img,
        'target_s': [target_s],
        'target_weight_s': [target_weight_s],
        'target_q': None,
        'target_weight_q': None,
        'return_loss': False,
        'img_metas': [{'sample_skeleton': [state['skeleton']],
                       'query_skeleton': state['skeleton'],
                       'sample_point_descriptions': np.array([state['point_descriptions']]),
                       'sample_joints_3d': [kp_src_3d],
                       'query_joints_3d': kp_src_3d,
                       'sample_center': [kp_src_tensor.mean(dim=0)],
                       'query_center': kp_src_tensor.mean(dim=0),
                       'sample_scale': [
                           kp_src_tensor.max(dim=0)[0] -
                           kp_src_tensor.min(dim=0)[0]],
                       'query_scale': kp_src_tensor.max(dim=0)[0] -
                                      kp_src_tensor.min(dim=0)[0],
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
    load_checkpoint(model, checkpoint_path, map_location='cpu')
    model.to(model_device)
    model.eval()
    with torch.no_grad():
        outputs = model(**data)
    # visualize results
    vis_q_weight = target_weight_s[0]
    vis_q_image = q_img[0].detach().cpu().numpy().transpose(1, 2, 0)

    out = plot_query_results(vis_q_image, vis_q_weight, state['skeleton'], torch.tensor(outputs['points']).squeeze(0))
    return out, state


def update_examples(query_img, node_descriptions, edges):
    state = {
        'kp_src': [],
        'skeleton': edges_prompt_to_list(edges),
        'count': 0,
        'color_idx': 0,
        'prev_pt': None,
        'prev_pt_idx': None,
        'prev_clicked': None,
        'point_descriptions': descriptions_prompt_to_list(node_descriptions),
    }

    return node_descriptions, edges, query_img, state


with gr.Blocks() as demo:
    state = gr.State({
        'kp_src': [],
        'skeleton': [],
        'count': 0,
        'color_idx': 0,
        'prev_pt': None,
        'prev_pt_idx': None,
        'prev_clicked': None,
        'point_descriptions': None,
    })

    gr.Markdown('''
    # CapeX Demo
    We present a novel category agnostic pose estimation approach that utilizes support text-graphs 
    (graphs with text on its nodes), instead of the conventional techniques that use support images.
    By leveraging the abstraction power of text-graphs, CapeX showcases SOTA results on MP100 while dropping the need 
    of providing an annotated support image. 
    ### [Paper](https://arxiv.org/pdf/2406.00384) | [GitHub](https://github.com/matanr/capex) 
    ## Instructions
    1. Explain using text the desired keypoints. Pleaser refer to the example for the right format.
    2. Optionally provide a graph representing the connections between the keypoints. Pleaser refer to the example for the right format.
    3. Upload an image of the object you want to pose to the query image.
    4. Click **Evaluate** to pose the query image. 
    ''')
    with gr.Row():
        # Input block for node descriptions
        node_descriptions = gr.Textbox(label="Node Descriptions (String separated by commas)", lines=5, type="text",
                                     # value="left eye, right eye, nose, neck, root of tail, left shoulder, left elbow, "
                                     #       "left front paw, right shoulder, right elbow, right front paw, left hip, "
                                     #       "left knee, left back paw, right hip, right knee, right back paw"
                                       value="left eye, nose, right eye"
                                       )

        # Input block for edges
        edges = gr.Textbox(label="Edges (List of 2-valued lists representing connections)", lines=5, type="text",
                                 # value="[[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [3, 5], [5, 6], [6, 7], [3, 8], "
                                 #       "[8, 9], [9, 10], [4, 11], [11, 12], [12, 13], [4, 14], [14, 15], [15, 16]]"
                           value="[[0,1], [1,2]]"
                           )

        def set_initial_text_graph():
            text_graph, state = visualize_graph("left eye, nose, right eye", "[[0,1], [1,2]]", {})
            return text_graph

        text_graph = gr.Image(label="Text-graph visualization",
                              value=set_initial_text_graph,
                              type="pil", height=400, width=400)

    with gr.Row():
        query_img = gr.Image(label="Query Image",
                             type="pil", height=400, width=400)
    with gr.Row():
        eval_btn = gr.Button(value="Evaluate")
    with gr.Row():
        output_img = gr.Plot(label="Output Image")
    with gr.Row():
        gr.Markdown("## Examples")
    with gr.Row():
        gr.Examples(
            examples=[
                ['examples/animal.png',
                 "left eye, right eye, nose, neck, root of tail, left shoulder, left elbow, "
                 "left front paw, right shoulder, right elbow, right front paw, left hip, "
                 "left knee, left back paw, right hip, right knee, right back paw",
                 "[[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [3, 5], [5, 6], [6, 7], [3, 8], [8, 9],"
                 "[9, 10], [4, 11], [11, 12], [12, 13], [4, 14], [14, 15], [15, 16]]"
                 ],
                ['examples/person.png',
                 "nose, left eye, right eye, left ear, right ear, left shoulder, right shoulder, left elbow, "
                 "right elbow, left wrist, right wrist, left hip, right hip, left knee, right knee, left ankle, "
                 "right ankle",
                 "[[15, 13], [13, 11], [16, 14], [14, 12], [11, 12], [5, 11], [6, 12], [5, 6], [5, 7],"
                 "[6, 8], [7, 9], [8, 10], [1, 2], [0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]"
                 ],
                ['examples/chair.png',
                 "left and front leg, right and front leg, right and back leg, left and back leg, "
                 "left and front side of the seat, right and front side of the seat, right and back side of the seat, "
                 "left and back side of the seat, top left side of the backseat, top right side of the backseat",
                 "[[0, 4], [3, 7], [1, 5], [2, 6], [4, 5], [5, 6], [6, 7], [7, 4], [6, 7], [7, 8],[8, 9], [9, 6]]",
                 ],
                ['examples/car.png',
                 "front and right wheel, front and left wheel, rear and right wheel, rear and left wheel, "
                 "right headlight, left headlight, right taillight, left taillight, "
                 "front and right side of the top, front and left side of the top, rear and right side of the top, "
                 "rear and left side of the top",
                 "[[0, 2], [1, 3], [0, 1], [2, 3], [8, 10], [9, 11], [8, 9], [10, 11], [4, 0], "
                 "[4, 8], [4, 5], [5, 1], [5, 9], [6, 2], [6, 10], [7, 3], [7, 11], [6, 7]]"
                 ]
            ],
            inputs=[query_img, node_descriptions, edges],
            outputs=[node_descriptions, edges, query_img, state],
            fn=update_examples,
            run_on_click=True,
        )

    eval_btn.click(fn=process,
                   inputs=[query_img, node_descriptions, edges, state],
                   outputs=[output_img, state])

    node_descriptions.change(visualize_graph, inputs=[node_descriptions, edges, state], outputs=[text_graph, state])
    edges.change(visualize_graph, inputs=[node_descriptions, edges, state], outputs=[text_graph, state])

    # visualize_button.click(fn=visualize_graph,
    #                inputs=[node_descriptions, edges, state],
    #                outputs=[text_graph, state])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CapeX Demo')
    parser.add_argument('--checkpoint',
                        help='checkpoint path',
                        default='./swin-gte-split1.pth')
    args = parser.parse_args()
    checkpoint_path = args.checkpoint
    demo.launch()

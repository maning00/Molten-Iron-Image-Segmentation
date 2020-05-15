import sys, os
import tensorflow as tf
import subprocess

sys.path.append("models")
from models.FC_DenseNet_Tiramisu import build_fc_densenet
from models.Encoder_Decoder import build_encoder_decoder
from models.RefineNet import build_refinenet
from models.FRRN import build_frrn
from models.MobileUNet import build_mobile_unet
from models.GCN import build_gcn
from models.DenseASPP import build_dense_aspp
from models.DDSC import build_ddsc
from models.BiSeNet import build_bisenet

SUPPORTED_FRONTENDS = ["ResNet50", "ResNet101", "ResNet152", "MobileNetV2", "InceptionV4"]

def download_checkpoints(model_name):
    subprocess.check_output(["python", "utils/get_pretrained_checkpoints.py", "--model=" + model_name])



def build_model(model_name, net_input, num_classes, crop_width, crop_height, frontend="ResNet101", is_training=True):
    # Get the selected model.
    # Some of them require pre-trained ResNet

    print("Preparing the model ...")


    if frontend not in SUPPORTED_FRONTENDS:
        raise ValueError("The frontend you selected is not supported. The following models are currently supported: {0}".format(SUPPORTED_FRONTENDS))

    if "ResNet50" == frontend and not os.path.isfile("models/resnet_v2_50.ckpt"):
        download_checkpoints("ResNet50")
    if "ResNet101" == frontend and not os.path.isfile("models/resnet_v2_101.ckpt"):
        download_checkpoints("ResNet101")
    if "ResNet152" == frontend and not os.path.isfile("models/resnet_v2_152.ckpt"):
        download_checkpoints("ResNet152")
    if "MobileNetV2" == frontend and not os.path.isfile("models/mobilenet_v2.ckpt.data-00000-of-00001"):
        download_checkpoints("MobileNetV2")
    if "InceptionV4" == frontend and not os.path.isfile("models/inception_v4.ckpt"):
        download_checkpoints("InceptionV4")

    network = None
    init_fn = None
    # BiSeNet requires pre-trained ResNet weights
    network, init_fn = build_bisenet(net_input, preset_model = model_name, frontend=frontend, num_classes=num_classes, is_training=is_training)
    return network, init_fn

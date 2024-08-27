import random

import cv2
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import torch
from torchvision.utils import make_grid

"""
General utilities to help with implementation
"""


def reset_seed(number):
    """
    Reset random seed to the specific number

    Inputs:
    - number: A seed number to use
    """
    random.seed(number)
    torch.manual_seed(number)
    return


import os

import numpy as np
import tifffile as tiff
from tqdm import tqdm

def load(directory='./data/HPC2/'):
    return normalize(tiff.imread(directory))

def normalize(frame):
    norm_frame = (frame - frame.min()) / (frame.max() - frame.min())
    norm_frame = norm_frame.astype(np.float32)
    return norm_frame


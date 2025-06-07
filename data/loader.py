import os
import tifffile as tiff
from tqdm import tqdm

def load(directory='./data/HPC2/', file: str = None):
    frames = {}
    if file:
        frames[file] = normalize(tiff.imread(os.path.join(directory, file)))
    else:
        for file in tqdm(os.listdir('./data/HPC2/')):
            frames[file] = normalize(tiff.imread(os.path.join(directory, file)))
    return frames

def normalize(frame):
    norm_frame = (frame - frame.min()) / (frame.max() - frame.min())
    norm_frame = (norm_frame * 255).astype('uint8')
    return norm_frame


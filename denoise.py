from data import loader
from denoising.HYPERPARAMS import *
from denoising.tv import tv_minimization_filter
import time

print("Loading video")
vid = loader.load("data/HPC2/", "00_02.tif")["00_02.tif"][:7000]

print(f"Applying TV minimization filter on {vid.shape[0]} frames")
start = time.time()
output_vid = tv_minimization_filter(vid, hyperparams=OPT_HYPER_TV_MINIMIZATION)

np.save("outputs/tv_1000_hpc2.npy", output_vid)
print(f"Time taken to denoise: {time.time() - start:.2f} seconds")

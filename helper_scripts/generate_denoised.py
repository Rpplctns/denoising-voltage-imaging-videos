import os

from data import loader
from denoising.HYPERPARAMS import *
from denoising.anisotropic import anisotropic_filter
from denoising.bilateral import bilateral_filter
from denoising.gaussian import gaussian_filter
from denoising.wavelet import wavelet_filter
import time
from denoising.tv import tv_minimization_filter

methods = [
    (anisotropic_filter, OPT_HYPER_ANISOTROPIC, "ani"),
    (bilateral_filter, OPT_HYPER_BILATERAL, "bi"),
    (gaussian_filter, OPT_HYPER_GAUSSIAN, "gaus"),
    (tv_minimization_filter, OPT_HYPER_TV_MINIMIZATION, "tv"),
    (wavelet_filter, OPT_HYPER_WAVELET, "wv")
]

for method, hyperparams, prefix in methods:
    for i in range(1, 6):
        if os.path.exists(f"outputs/{prefix}_optosynth_{i}.npy"):
            print(f"Skipping {prefix}_ptosynth_{i} as it already exists")
            continue
        print("Loading video")
        vid = loader.load(f"data/optosynth/raw/optosynth__{i}__20__5.tif")
        print(f"Applying the algorithm on {vid.shape[0]} frames")
        start = time.time()
        output_vid = method(vid, hyperparams=hyperparams)
        print(f"Time taken to denoise: {time.time() - start:.2f} seconds")
        np.save(f"outputs/{prefix}_optosynth_{i}.npy", output_vid)
        del(vid)
        del(output_vid)

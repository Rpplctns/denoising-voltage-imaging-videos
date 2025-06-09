import numpy as np
from skimage.restoration import denoise_nl_means

def nl_means(vid, hyperparams=None):
    if hyperparams is None:
        hyperparams = {
            "patch_size": 5,
            "patch_distance": 6,
            "h": 0.1
        }

    patch_size = hyperparams["patch_size"]
    patch_distance = hyperparams["patch_distance"]
    h = hyperparams["h"]

    output_vid = denoise_nl_means(
        vid,
        patch_size=patch_size,
        patch_distance=patch_distance,
        h=h,
        fast_mode=True
    )

    return output_vid

from scipy.ndimage import zoom
from skimage.restoration import denoise_tv_chambolle

def tv_minimization_filter(vid, hyperparams=None):
    if hyperparams is None:
        hyperparams = {"weight": 0.1, "spacing_ratio": 1}

    weight = hyperparams["weight"]
    spacing_ratio = hyperparams["spacing_ratio"]

    rescaled = zoom(vid, (1, spacing_ratio, spacing_ratio), order=1)
    filtered = denoise_tv_chambolle(rescaled, weight=weight, max_num_iter=200, eps=0.0002)
    output_vid = zoom(filtered, (1, 1 / spacing_ratio, 1 / spacing_ratio), order=1)

    return output_vid

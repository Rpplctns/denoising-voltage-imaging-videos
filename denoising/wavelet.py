from scipy.ndimage import zoom
from skimage.restoration import denoise_wavelet

def wavelet_filter(vid, hyperparams=None):
    if hyperparams is None:
        hyperparams = {"wavelet": "haar", "mode": "soft", "spacing_ratio": 1}
    wavelet = hyperparams["wavelet"]
    mode = hyperparams["mode"]
    spacing_ratio = hyperparams["spacing_ratio"]

    rescaled = zoom(vid, (1, spacing_ratio, spacing_ratio), order=1)
    filtered = denoise_wavelet(rescaled, wavelet=wavelet, mode=mode)
    output_vid = zoom(filtered, (1, 1 / spacing_ratio, 1 / spacing_ratio), order=1)
    return output_vid

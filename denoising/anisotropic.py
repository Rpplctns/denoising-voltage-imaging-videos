from medpy.filter import anisotropic_diffusion
from scipy.ndimage import zoom

def anisotropic_filter(vid, hyperparams=None):
    if hyperparams is None:
        hyperparams = {"niter": 10, "kappa": 50, "gamma": 0.1, "spacing_ratio": 1}

    niter = hyperparams["niter"]
    kappa = hyperparams["kappa"]
    gamma = hyperparams["gamma"]
    spacing_ratio = hyperparams["spacing_ratio"]

    rescaled = zoom(vid, (1, spacing_ratio, spacing_ratio), order=1)
    filtered = anisotropic_diffusion(rescaled, niter=niter, kappa=kappa, gamma=gamma, option=1)
    output_vid = zoom(filtered, (1, 1 / spacing_ratio, 1 / spacing_ratio), order=1)
    return output_vid

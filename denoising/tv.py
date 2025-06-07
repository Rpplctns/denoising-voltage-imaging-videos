from skimage.restoration import denoise_tv_chambolle

def tv_minimization_filter(vid, hyperparams=None):
    if hyperparams is None:
        hyperparams = {"weight": 0.1}

    weight = hyperparams["weight"]

    output_vid = denoise_tv_chambolle(vid, weight=weight, max_num_iter=200, eps=0.0002)
    return output_vid

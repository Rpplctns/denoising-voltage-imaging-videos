import numpy as np
from tqdm import tqdm

def eval_denoising_method(vid, method_denoise, method_eval, hyperparam_array):
    result = np.zeros_like(hyperparam_array)

    for idx in tqdm(np.ndindex(hyperparam_array.shape)):
        result[idx] = method_eval(method_denoise(vid, hyperparam_array[idx]))

    return result

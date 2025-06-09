import numpy as np
from tqdm import tqdm

def eval_denoising_method(vid, method_denoise, method_eval, hyperparam_array, name):
    print(f"Working on {name}. Number of items: {np.prod(hyperparam_array.shape)}")

    result = np.zeros_like(hyperparam_array)

    for idx in tqdm(np.ndindex(hyperparam_array.shape)):
        denoised = method_denoise(vid, hyperparam_array[idx])
        result[idx] = method_eval(denoised)
        del(denoised)

    np.save(f"results_params/{name}.npy", result)
    np.save(f"results_params/{name}_H.npy", hyperparam_array)

    return result

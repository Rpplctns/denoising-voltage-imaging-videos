from data import loader
from skimage.metrics import structural_similarity as ssim
from denoising.HYPERPARAMS import *
from denoising.bilateral import bilateral_filter
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


data = loader.load(directory='data/optosynth/raw/optosynth__1__20__5.tif')
data_gt = loader.load(directory='data/optosynth/clean/optosynth__1__20__5.tif')

eval_denoising_method(
    data[:1000],
    bilateral_filter,
    lambda denoised: ssim(denoised, data_gt[:1000], data_range=0.1, multichannel=False),
    HYPER_BILATERAL,
    f'bi_ssim_1000f'
)

from data import loader
from skimage.metrics import structural_similarity as ssim
from denoising.HYPERPARAMS import *
from denoising.bilateral import bilateral_filter
from eval import eval_denoising_method
data = loader.load(directory='data/optosynth/raw/', file='optosynth__1__20__5.tif')['optosynth__1__20__5.tif']
data_gt = loader.load(directory='data/optosynth/clean/', file='optosynth__1__20__5.tif')['optosynth__1__20__5.tif']

eval_denoising_method(
            data[:300],
            bilateral_filter,
            lambda denoised: ssim(denoised, data_gt[:300], data_range=0.1, multichannel=False),
            HYPER_BILATERAL,
            f'WIN_bilateral_ssim_1000f'
)

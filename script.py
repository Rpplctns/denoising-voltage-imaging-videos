from data import loader
from skimage.metrics import structural_similarity as ssim
from denoising.HYPERPARAMS import *
from denoising.gaussian import gaussian_filter
from eval import eval_denoising_method
data = loader.load(directory='data/optosynth/raw/', file='optosynth__1__20__5.tif')['optosynth__1__20__5.tif']
data_gt = loader.load(directory='data/optosynth/clean/', file='optosynth__1__20__5.tif')['optosynth__1__20__5.tif']

eval_denoising_method(
            data[:1000],
            gaussian_filter,
            lambda denoised: ssim(denoised, data_gt[:1000], data_range=0.1, multichannel=False),
            HYPER_GAUSSIAN,
            f'WIN_gaussian_ssim_1000f'
)

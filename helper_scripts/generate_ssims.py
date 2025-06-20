import numpy as np
from data import loader
from skimage.metrics import structural_similarity as ssim

methods = ["ani", "bi", "gaus", "tv", "wv"]

for prefix in methods:
      res = []
      for i in range(1, 6):
            gt = loader.load(f"data/optosynth/clean/optosynth__{i}__20__5.tif")
            vid = np.load(f"outputs/{prefix}_optosynth_{i}.npy", allow_pickle=True)
            res += [ssim(gt, vid, data_range=0.1, multichannel=False)]
      print(f"Method: {prefix}, SSIM: {np.mean(res):.4f} ± {np.std(res):.4f}")

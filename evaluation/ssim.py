import numpy as np

def ssim(vid1, vid2, k1=0.01, k2=0.03, L=255):
    assert vid1.shape == vid2.shape
    assert len(vid1.shape) == 3
    c1 = (k1 * L) ** 2
    c2 = (k2 * L) ** 2
    ssim_values = []
    for i in range(vid1.shape[0]):
        frame1 = vid1[i]
        frame2 = vid2[i]
        mu1 = frame1.mean()
        mu2 = frame2.mean()
        var1 = frame1.var()
        var2 = frame2.var()
        covar = ((frame1 - mu1) * (frame2 - mu2)).mean()
        ssim_values += [
            (2 * mu1 * mu2 + c1) * (2 * covar + c2) /
            ((mu1 ** 2 + mu2 ** 2 + c1) * (var1 + var2 + c2))
        ]
    return np.mean(ssim_values)

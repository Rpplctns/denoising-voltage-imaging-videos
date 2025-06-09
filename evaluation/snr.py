import numpy as np

def temporal_snr(vid):
    mean = np.mean(vid, axis=0)
    sd = np.std(vid, axis=0)
    with np.errstate(divide='ignore', invalid='ignore'):
        snr = np.where(sd != 0, mean / sd, 0)
    return np.mean(snr), np.percentile(snr, 25)

def sliding_window_tsnr(vid, window_size=100, step = 20):
    values = []
    for i in range(0, vid.shape[0] - window_size, step):
        values += [temporal_snr(vid[i: i + window_size])]
    return np.mean(values), np.std(values)

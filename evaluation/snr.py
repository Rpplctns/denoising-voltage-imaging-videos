import numpy as np

def snr_with_background(vid, background):
    background_mean = np.mean(background)
    signal = np.mean(vid**2)
    noise = np.mean((vid - background_mean)**2)
    snr_value = 10 * np.log10(signal / noise)
    return snr_value

import numpy as np

HYPER_GAUSSIAN = np.array([
    [[{"kernel_size": 5, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10} for sigma_xy in range(2, 9, 3)] for sigma_t in range(2, 21, 4)],
    [[{"kernel_size": 7, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10} for sigma_xy in range(2, 9, 3)] for sigma_t in range(2, 21, 4)],
    [[{"kernel_size": 9, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10} for sigma_xy in range(2, 9, 3)] for sigma_t in range(2, 21, 4)],
])

HYPER_BILATERAL = np.array([
    [[[{"kernel_size": 5, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10, "sigma_intensity": sigma_intensity} for sigma_xy in range(6, 15, 2)] for sigma_t in range(6, 15, 2)] for sigma_intensity in range(20, 30, 3)],
    [[[{"kernel_size": 7, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10, "sigma_intensity": sigma_intensity} for sigma_xy in range(6, 15, 2)] for sigma_t in range(6, 15, 2)] for sigma_intensity in range(20, 30, 3)],
    [[[{"kernel_size": 9, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10, "sigma_intensity": sigma_intensity} for sigma_xy in range(6, 15, 2)] for sigma_t in range(6, 15, 2)] for sigma_intensity in range(20, 30, 3)],
])

HYPER_ANISOTROPIC = np.array([
    [
        [
            [
                {"niter": niter, "kappa": kappa / 100, "gamma": gamma / 100, "spacing_ratio": spacing_ratio}
                for niter in range(3, 22, 3)
            ]
            for kappa in range(2, 15, 3)
        ]
        for gamma in range(3, 9, 3)
    ]
    for spacing_ratio in [0.5, 0.75, 1.0, 1.33, 2]
])

HYPER_WAVELET = np.array([
    [
        [
            {"wavelet": wavelet, "mode": mode, "spacing_ratio": spacing_ratio}
            for wavelet in ["haar", "db4", "sym5"]
        ]
        for mode in ["soft", "hard"]
    ]
    for spacing_ratio in [0.5, 0.75, 1.0, 1.33, 2]
])

HYPER_TV_MINIMIZATION = np.array([
    [
        {"weight": weight / 1000, "spacing_ratio": spacing_ratio}
        for weight in range(2, 21, 2)
    ]
    for spacing_ratio in [0.5, 0.75, 1.0, 1.33, 2]
])

HYPER_NL_MEANS = np.array([
    [
        [
            {"patch_size": patch_size, "patch_distance": patch_distance, "h": h}
            for patch_size in [3, 5]
        ]
        for patch_distance in [5, 7, 9, 80, 90, 100]
    ]
    for h in [0.05, 0,1, 0.15, 0.2, 0.3, 0.5]
])

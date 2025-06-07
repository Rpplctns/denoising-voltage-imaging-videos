import numpy as np

HYPER_GAUSSIAN = np.array([
    [[{"kernel_size": 5, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10} for sigma_xy in range(6, 15, 2)] for sigma_t in range(6, 15, 2)],
    [[{"kernel_size": 7, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10} for sigma_xy in range(6, 15, 2)] for sigma_t in range(6, 15, 2)],
    [[{"kernel_size": 9, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10} for sigma_xy in range(6, 15, 2)] for sigma_t in range(6, 15, 2)],
])

HYPER_BILATERAL = np.array([
    [[[{"kernel_size": 5, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10, "sigma_intensity": sigma_intensity} for sigma_xy in range(6, 15, 2)] for sigma_t in range(6, 15, 2)] for sigma_intensity in range(20, 30, 3)],
    [[[{"kernel_size": 7, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10, "sigma_intensity": sigma_intensity} for sigma_xy in range(6, 15, 2)] for sigma_t in range(6, 15, 2)] for sigma_intensity in range(20, 30, 3)],
    [[[{"kernel_size": 9, "sigma_xy": sigma_xy / 10, "sigma_t": sigma_t / 10, "sigma_intensity": sigma_intensity} for sigma_xy in range(6, 15, 2)] for sigma_t in range(6, 15, 2)] for sigma_intensity in range(20, 30, 3)],
])

HYPER_ANISOTROPIC = [
    [
        [
            [
                {"niter": niter, "kappa": kappa, "gamma": gamma / 10, "spacing_ratio": spacing_ratio}
                for niter in range(10, 21, 2)
            ]
            for kappa in range(20, 41, 5)
        ]
        for gamma in range(1, 4)
    ]
    for spacing_ratio in [0.5, 0.75, 1.0, 1.33, 2]
]

HYPER_WAVELET = [
    [
        [
            {"wavelet": wavelet, "mode": mode, "spacing_ratio": spacing_ratio}
            for wavelet in ["haar", "db1", "sym2", "coif1"]
        ]
        for mode in ["soft", "hard"]
    ]
    for spacing_ratio in [0.5, 0.75, 1.0, 1.33, 2]
]

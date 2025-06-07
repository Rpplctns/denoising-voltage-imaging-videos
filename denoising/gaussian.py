import numpy as np

def gaussian_filter(vid, hyperparams=None):
    if hyperparams is None:
        hyperparams = {"kernel_size": 5, "sigma_xy": 1.0, "sigma_t": 1.0}

    kernel_size = hyperparams["kernel_size"]
    sigma_xy = hyperparams["sigma_xy"]
    sigma_t = hyperparams["sigma_t"]

    lin = np.arange(-(kernel_size // 2), kernel_size // 2 + 1)
    kernel_xy = np.exp(-0.5 * (lin / sigma_xy) ** 2)
    kernel_t = np.exp(-0.5 * (lin / sigma_t) ** 2)
    
    kernel = np.outer(kernel_xy, kernel_xy).reshape(1, kernel_size, kernel_size) * kernel_t.reshape(kernel_size, 1, 1)
    kernel /= np.sum(kernel)

    output_vid = np.zeros_like(vid)
    for i in range(vid.shape[0]):
        for j in range(vid.shape[1]):
            for k in range(vid.shape[2]):
                if i < kernel_size // 2 or i >= vid.shape[0] - kernel_size // 2 or \
                   j < kernel_size // 2 or j >= vid.shape[1] - kernel_size // 2 or \
                   k < kernel_size // 2 or k >= vid.shape[2] - kernel_size // 2:
                    output_vid[i, j, k] = vid[i, j, k]
                else:
                    patch = vid[
                            (i - kernel_size // 2):(i + kernel_size // 2 + 1),
                            (j - kernel_size // 2):(j + kernel_size // 2 + 1),
                            (k - kernel_size // 2):(k + kernel_size // 2 + 1)
                        ]
                    output_vid[i, j, k] = np.sum(kernel * patch)
    return output_vid

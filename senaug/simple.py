"""Simple transform augmentations.

- Author: Jongkuk Lim
- Contact: lim.jeikei@gmail.com
"""


import numpy as np


def jitter(x: np.ndarray, sigma: float = 0.1) -> np.ndarray:
    """Add a random jittering.

    Args:
        x: sensor data.
        sigma: amount of the noise.

    Returns:
        x + normal random with sigma STD.
    """
    jitter_noise = np.random.normal(loc=0, scale=sigma, size=x.shape)

    return x + jitter_noise


def scale(x: np.ndarray, sigma: float = 0.1) -> np.ndarray:
    """Scale a given matrix.

    Args:
        x: sensor data.
        sigma: scaling factor

    Returns:
        randomly scaled matrix.
    """
    scale_factor = np.random.normal(loc=1.0, scale=sigma, size=(1, x.shape[1]))
    scale_factor = np.matmul(np.ones((x.shape[0], 1)), scale_factor)

    return x * scale_factor

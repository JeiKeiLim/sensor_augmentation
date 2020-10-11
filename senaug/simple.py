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

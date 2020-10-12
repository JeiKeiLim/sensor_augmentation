"""Warp transform augmentations.

- Author: Jongkuk Lim
- Contact: lim.jeikei@gmail.com
"""

from typing import Tuple

import numpy as np
from scipy.interpolate import CubicSpline


def generate_random_curves(shape: Tuple, sigma: float = 0.2, knot: int = 4):
    """Generate random smooth curves for augmentation purpose.

    Args:
        shape: sensor data shape to generate random curves.
        sigma: random magnitude of the curves.
        knot: # of knots for the random curves (complexity of the curves)

    Returns:
        randomly generated curves.
    """
    xx = (
        np.ones((shape[1], 1)) * (np.arange(0, shape[0], (shape[0] - 1) / (knot + 1)))
    ).transpose()
    yy = np.random.normal(loc=1.0, scale=sigma, size=(knot + 2, shape[1]))
    x_range = np.arange(shape[0])
    cs_x = CubicSpline(xx[:, 0], yy[:, 0])
    cs_y = CubicSpline(xx[:, 1], yy[:, 1])
    cs_z = CubicSpline(xx[:, 2], yy[:, 2])

    return np.array([cs_x(x_range), cs_y(x_range), cs_z(x_range)]).transpose()


def warp_random_curves(x: np.ndarray, sigma: float = 0.2, knot: int = 4):
    """Augment sensor data x with randomly generated smoothed curves.

    Args:
        x: sensor data.
        sigma: random magnitude of the curves.
        knot: # of knots for the random curves (complexity of the curves)

    Returns:
        Randomly scaled matrix by random curves.
          x * random_curves
    """
    return x * generate_random_curves(x.shape, sigma=sigma, knot=knot)

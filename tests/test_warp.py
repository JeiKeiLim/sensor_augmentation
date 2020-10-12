"""Unit test for warp augmentation.

- Author: Jongkuk Lim
- Contact: lim.jeikei@gmail.com
"""

import numpy as np

import senaug


def test_warp_random_curves():
    x = np.ones((10, 3))
    y = senaug.warp_random_curves(x.copy(), sigma=0.1, knot=4)

    assert np.isclose(x, y, rtol=0.2).sum() > (x.size * 0.8)

import numpy as np

import senaug


def test_jitter():
    x = np.ones((100, 3))
    y = senaug.jitter(x.copy(), sigma=0.1)
    assert np.isclose(x, y, rtol=0.2).sum() > x.size * 0.8


def test_scale():
    x = np.tile(np.linspace(0, 1.0, 10), (3, 1)).T
    y = senaug.scale(x.copy(), sigma=0.1)

    assert np.isclose(y.max(axis=0), np.array([1.0, 1.0, 1.0]), rtol=0.2).sum() > 2


if __name__ == "__main__":
    test_jitter()

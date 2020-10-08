import numpy as np

from senaug import simple


def test_jitter():
    x = np.ones((100, 3))
    y = simple.jitter(x.copy(), sigma=0.1)
    assert np.isclose(x, y, rtol=0.2).sum() > x.size * 0.8


if __name__ == "__main__":
    test_jitter()

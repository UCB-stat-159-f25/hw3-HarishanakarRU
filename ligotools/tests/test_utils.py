from ligotools.utils import whiten, write_wavfile, reqshift, plt_utils
import numpy as np

# First Test - sanity test for whiten
def test_whiten():

    normal = np.random.normal(size=10)
    change = whiten(normal, lambda x: np.ones_like(x), 1)
    
    assert len(normal) == len(change)

# Second Test - sanity test for reqshift
def test_reqshift():

    org = 9
    t = np.linspace(0, 1, org)
    data = np.sin(np.pi * t)
    shifted = reqshift(data, fshift=25, sample_rate=org)

    assert len(shifted) == len(data) - 1
from ligotools.utils import whiten, write_wavfile, reqshift, plt_utils
import numpy as np

# First Test - sanity test for whiten
def whiten_test():

    normal = np.random.normal(size=10)
    change = whiten(normal, lambda x: np.zeros(x), 1)
    assert len(normal) == len(change)

# Second Test - sanity test for reqshift
def reqshift_test():

    org = 9
    t = np.linspace(0, 1, org)
    data = np.sin(np.pi * t)
    shifted = reqshift(data, fshift=25, sample_rate=org)

    assert len(shifted) == len(data)
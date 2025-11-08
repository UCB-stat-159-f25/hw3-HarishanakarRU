from ligotools import *
import numpy as np

# First Test
def test_dq_channel_to_seglist():

    a = np.array([1, 2, 3, 4, 5])
    sgs = dq_channel_to_seglist(a, fs=1)
    s = sgs[0]

    assert len(sgs) == 1
    assert s.stop == 4

# Second Test
def test_dq2segs():

    z = np.array([0, 1, 1, 0])
    s = 100
    seglist = dq2segs(z, s)
    start, stop = seglist.seglist[0]
    
    assert start == 101
    assert stop == 103

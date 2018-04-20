import unittest
import numpy as np
import diehard as dh

class TestOPERM(unittest.TestCase):
    def test_existence(self):
        assert dh.cat

    def test_run(self):
        arr = np.random.random(1000000)
        out = dh.cat(arr)
        assert isinstance(out, dict)

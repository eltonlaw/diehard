import unittest
import numpy as np
import diehard as dh

class TestBirthday(unittest.TestCase):
    def test_existence(self):
        assert dh.birthday

    def test_run(self): 
    	samples = [np.random.randint(0, 2**32, 512) for i in range(100)]
    	out = dh.birthday.birthday(samples)
    	assert isinstance(out, float)
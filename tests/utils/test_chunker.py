import unittest
import numpy as np
from diehard.utils import chunker
# pylint:disable=missing-docstring

class TestChunker(unittest.TestCase):
    def test_overlapping_complete(self): 
        chunks = chunker(np.arange(100), 5, overlapping=True, complete=True)
        list(chunks)

    def test_overlapping(self): 
        chunks = chunker(np.arange(100), 5, overlapping=True, complete=False)
        list(chunks)

    def test_complete(self): 
        chunks = chunker(np.arange(100), 5, overlapping=False, complete=True)
        list(chunks)

    def test_default(self):
        chunks = chunker(np.arange(100), 5, overlapping=False, complete=False)
        list(chunks)

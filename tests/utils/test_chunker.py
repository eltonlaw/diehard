""" test_chunker.py """
import unittest
import numpy as np
from diehard.utils import chunker
# pylint:disable=missing-docstring
# pylint:disable=no-self-use

class TestChunker(unittest.TestCase):
    def test_overlapping_complete(self):
        chunks = chunker(np.arange(100), 5, skip=1, complete=True)
        list(chunks)

    def test_skip(self):
        chunks = chunker(np.arange(100), 5, skip=1, complete=False)
        list(chunks)

    def test_complete(self):
        chunks = chunker(np.arange(100), 5, skip=None, complete=True)
        list(chunks)

    def test_default(self):
        chunks = chunker(np.arange(100), 5, skip=None, complete=False)
        list(chunks)

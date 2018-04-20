""" overlapping_permutations.py """
import collections
import numpy as np
from diehard.utils import preprocess
from diehard.utils import chunker

@preprocess
def operm(arr, consecutive=5):
    """ Analyze sequences of n consecutive real numbers. All possible
    orderings should occur with statistically equal probability.

    PARAMETERS
    ----------
    arr: numpy.array
        1D list

    RETURNS
    -------
    collections.Counter
        Keys are the permutation of orderings possible. Value is the number
        of occurences found.
    """
    chunks = chunker(arr, consecutive, skip=1, complete=True)
    chunks_np = np.array(list(chunks))
    orderings = np.argsort(chunks_np)
    unique_counter = collections.Counter((map(tuple, orderings)))
    return unique_counter

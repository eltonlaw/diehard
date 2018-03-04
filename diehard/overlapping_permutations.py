""" overlapping_permutations.py """
import collections
import numpy as np
from diehard.utils import preprocess
from diehard.utils import chunker

@preprocess
def overlapping_permutations(arr, consecutive=5):
    """ Analyze sequences of n consecutive real numbers. All possible
    orderings should occur with statistically equal probability

    PARAMETERS
    ----------
    arr: numpy.array
        1D list

    RETURNS
    -------
    """
    # n_permutations = np.math.factorial(consecutive)
    chunks = chunker(arr, consecutive, overlapping=True, complete=True)
    chunks_np = np.array(list(chunks))
    orderings = np.argsort(chunks_np)
    unique_counter = collections.Counter((map(tuple, orderings)))

    # TODO: Compute variance analysis and randomness likelihood
    return unique_counter

""" overlapping_permutations.py """
from functools import wraps


@wraps
def preprocess(func):
    """ Standardizes inputs"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

def chunker(arr, batch_size, overlapping=False, complete=False):
    """ Chunk an array into smaller sequences

    complete:
        For only returning batches that have length n
    overlapping:
        For generating batches that overlap
    """
    skip = batch_size
    if overlapping:
        skip = 1

    start = 0
    end = len(arr)
    for i in range(start, end, skip):
        batch = arr[i:i+batch_size]
        if not complete or len(batch) == batch_size:
            yield batch
        else:
            break

@preprocess
def overlapping_permutations(arr, cons=5):
    """ Analyze sequences of n consecutive real numbers. All possible
    orderings should occur with statistically equal probability

    PARAMETERS
    ----------
    arr: numpy.array
        1D list

    RETURNS
    -------
    """
    chunks = chunker(arr, cons, overlapping=True, complete=True)
    list(chunks)

    chunks = chunker(arr, cons, overlapping=True, complete=False)
    list(chunks)

    chunks = chunker(arr, cons, overlapping=False, complete=False)
    list(chunks)

    chunks = chunker(arr, cons, overlapping=False, complete=True)
    list(chunks)

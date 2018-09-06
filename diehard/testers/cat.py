# -*- coding: utf-8 -*-
""" cat.py """
import string
import numpy as np
from diehard.utils import preprocess
from diehard.utils import chunker

@preprocess
def cat(arr, match="CAT", upper_bound=None, lower_bound=None):
    """
    Basic idea is if a monkey typed randomly, how long would it take for it
    to write `CAT`. Practically, we are mapping generated numbers onto the
    alphabet.

    >"There are 26**3 = 17 576 possible 3-letter words, so the average number of
    keystrokes necessary to produce CAT should be around 17 576" [1]

    Example
    ------- 
    

    Parameters
    ----------
    word: string or list-type object
        All elements of the string must be the same number of characters
    match: string or list-type object
        The keyword to search for. Other than length, doesn't really matter.
        If you pass in a list of strings, it will give you a result for each
        passed in string.
    upper_bound: int (optional)
        Upper bound of random values. If not set, will calculate the minimum
        value from the array passed.
    lower_bound: int (optional)
        Lower bound of random values. If not set, will calculate the maximum
        value from the array passed.

    Returns
    -------
    dict
        Key is the string passed into match, the value is a list of the
        iteration cycles it was found at

    Notes
    -----
    [1]: Marsaglia, G. and Zaman, A., (1995), Monkey tests for random number
    generators, Computers & Mathematics with Applications, 9, No. 9, 1–10.

    """
    if upper_bound is None:
        upper_bound = np.max(arr)
    if lower_bound is None:
        lower_bound = np.min(arr)

    if isinstance(match, str):
        match = [match]
    match = list(map(str.upper, match))
    num_letters = len(match[0])
    assert all([len(match_i) == num_letters for match_i in match]), \
            "All elements of `match` must have the same number of characters"

    n_uppercase = len(string.ascii_uppercase)
    # {...number: letter...} mapping
    mapping = dict(zip(range(n_uppercase), string.ascii_uppercase))

    # Scale the array so that everything is between 0 and 26
    arr_norm = np.floor((arr - lower_bound) * (n_uppercase/upper_bound))

    # Map the integer component to letters
    letters = [mapping[i] for i in arr_norm.astype(np.int)]
    # Split the array of letters into words
    words = chunker(letters, batch_size=num_letters, complete=True)

    iter_counts = {match_i: [] for match_i in match}
    for i, letter_list in enumerate(words):
        word = ''.join(letter_list)
        if word in match:
            iter_counts[word].append(i)

    return iter_counts

""" Utillity Decorators """
from functools import wraps
import numpy as np
# pylint: disable=missing-docstring

def preprocess(func):
    """ Standardizes inputs"""
    @wraps(func)
    def wrapper(arr, **kwargs):
        if isinstance(arr, list):
            arr = np.array(arr)
        return func(arr, **kwargs)
    return wrapper

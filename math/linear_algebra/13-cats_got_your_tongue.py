#!/usr/bin/env python3
"""function concatenates two matrices along axis using numpy"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """returns new numpy.ndarray"""
    return np.concatenate((mat1, mat2), axis=axis)

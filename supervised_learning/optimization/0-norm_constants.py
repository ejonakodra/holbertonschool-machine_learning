#!/usr/bin/env python3
"""Function calculates the normalization constants of a matrix"""


import numpy as np


def normalization_constants(X):
    """Calculates the mean and standard deviation of each feature
    in the input matrix X."""
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)

    return mean, std

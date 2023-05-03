#!/usr/bin/env python3
"""Function shuffles the data point in two matrices the same way"""

import numpy as np


def shuffle_data(X, Y):
    """Shuffles the data points in two matrices the same way"""
    m = X.shape[0]
    permutation = np.random.permutation(m)
    X_shuffled = X[permutation]
    Y_shuffled = Y[permutation]
    return X_shuffled, Y_shuffled

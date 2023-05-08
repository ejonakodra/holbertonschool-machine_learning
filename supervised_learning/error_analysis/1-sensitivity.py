#!/usr/bin/env python3
"""Function calculates the sensitivity for each class
in a confusion matrix"""


import numpy as np


def sensitivity(confusion):
    """funtion returns numpy.ndarray of shape (classes,)
    containing sensitivity of each class"""
    tp = np.diag(confusion)
    fn = np.sum(confusion, axis=1) - tp
    tpr = tp / (tp + fn)
    return tpr

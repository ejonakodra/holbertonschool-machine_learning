#!/usr/bin/env python3
"""Function calculates the precision for each class in a confusion matrix """


import numpy as np


def precision(confusion):
    """function returns numpy.ndarray of shape (classes,) 
    containing precision of each class"""
    tp = np.diag(confusion)
    precision = tp / (tp + fp)
    return precision

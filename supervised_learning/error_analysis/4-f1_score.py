#!/usr/bin/env python3
"""Function that calculates the F1 score for each class in a confusion matrix"""


import numpy as np


def f1_score(confusion):
    """function returns numpy.ndarray of shape (classes,) containing F1 score of each class"""
    p = precision(confusion)
    r = specificity(confusion)
    f1 = 2 * p * r / (p + r)
    return f1

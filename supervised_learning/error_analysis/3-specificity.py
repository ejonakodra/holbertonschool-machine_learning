#!/usr/bin/env python3
"""Function calculates the specificity for each class in a confusion matrix"""


import numpy as np


def specificity(confusion):
    """funtion returns numpy.ndarray of shape (classes,)
     containing specificity of each class"""
    tp = np.diag(confusion)
    fn = np.sum(confusion, axis=1) - tp
    fp = np.sum(confusion, axis=0) - tp
    tn = confusion.sum() - (tp + fp + fn)
    return tn / (tn + fp)

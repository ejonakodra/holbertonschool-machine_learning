#!/usr/bin/env python3
"""Function creates a confusion matrix"""


import numpy as np


def create_confusion_matrix(labels, logist):
    """function returns a confusion matrix
    [numpy.ndarray of shape (classes, classes)]:
    row indices represent correct labels
    column indices represent predicted labels"""

    return np.matmul(labels.transpose(), logist)

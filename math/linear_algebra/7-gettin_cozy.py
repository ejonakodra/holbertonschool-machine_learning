#!/usr/bin/env python3
"""defines function that concatenates two 2D matrices along an axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """returns new matrix that is the concatenation of two 2D matrices"""
    if axis == 0: #columns
        if len(mat1[0]) != len(mat2[0]):
            return None
        result = mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        result = [mat1[i] + mat2[i] for i in range(len(mat1))]
        else:
            return None
        return result

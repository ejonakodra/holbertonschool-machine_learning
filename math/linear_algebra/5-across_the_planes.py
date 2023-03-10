#!/usr/bin/env python3
"""function returns the sum of two matrix"""


def add_matrices2D(mat1, mat2):
    """check if we can add the mat,then return the sum"""
    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None
    mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        mat.append(row)
    return mat

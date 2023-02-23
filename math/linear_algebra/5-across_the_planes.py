#!/usr/bin/env python3
"""function returns the sum of two matrix"""

def add_matrices2D(mat1, mat2):
    """check if mat1 and mat2 does not have the same shape else return the sum"""
    if (len(mat1) != len(mat2)) or (len(mat1[0]) != len(mat2[0])):
        return None
    result = [[mat1[i][j] + mat2[i][j]  for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result

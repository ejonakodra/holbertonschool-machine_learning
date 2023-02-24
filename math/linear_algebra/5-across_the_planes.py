#!/usr/bin/env python3
"""function returns the sum of two matrix"""

def add_matrices2D(mat1, mat2):
    """check if len mat1 and let mat2 match then rertun the sum matrix"""
    mat = []
    if len(mat1[0]) != len(mat2[0]) or len(mat1) != len(mat2):
        return None
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
            mat.append(row)
    return mat
                                                                                                                                 
    

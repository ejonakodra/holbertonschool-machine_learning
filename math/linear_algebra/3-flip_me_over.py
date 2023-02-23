#!/usr/bin/env python3
"""function returns the transposed matrix"""


def matrix_transpose(matrix):
    "solution using list comprehension"
    t = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return t

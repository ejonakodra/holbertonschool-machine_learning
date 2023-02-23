#!/usr/bin/env python3
"""function returns the transposed matrix"""


def matrix_transpose(matrix):
    "solution using list comprehension"
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix

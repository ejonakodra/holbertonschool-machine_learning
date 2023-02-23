#!/usr/bin/env python3
""" this function returns the shape of a matrix"""


def matrix_shape(matrix):
    """ returns list of integers representing dimensions of a given matrix """
    shape = []
    while (type(matrix) is list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape

#!/usr/bin/env python3
""" function that performs element-wise operations on two matrices """


def np_elementwise(mat1, mat2):
    """returns tuple containing element-wise sum, difference, product, quotient"""
    result = []
    result.append(mat1 + mat2)
    result.append(mat1 - mat2)
    result.append(mat1 * mat2)
    result.append(mat1 / mat2)
    return tuple(result)
                

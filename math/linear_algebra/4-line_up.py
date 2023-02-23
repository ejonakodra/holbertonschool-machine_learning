#!/usr/bin/env python3
"""function returns the sum of two arrays"""


def add_arrays(arr1, arr2):
    """check if length of arrays do not match else return the sum"""
    if len(arr1) != len(arr2):
        return None
    sum_array = []
    for i in range(len(arr1)):
        sum_array.append(arr1[i] + arr2[i])
    return sum_array

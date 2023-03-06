#!/usr/bin/env python3
""""function that returns sigma sum"""


def summation_i_squared(n):
    """check if n is valid, then return n"""
    if type(n) is not int or n < 1:
        return None
    sigma_sum = (n * (n + 1) * ((2 * n) + 1))/6
    return int(sigma_sum)

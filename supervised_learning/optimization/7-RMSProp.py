#!/usr/bin/env python3
"""Function that updates a variable
using RMSProp optimization algorithm"""


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """Updates a variable using RMSProp optimization algorithm"""
    s_dW = (beta2 * s) + ((1 - beta2) * (grad ** 2))
    var -= alpha * (grad / (epsilon + (s_dW ** (1 / 2))))
    return var, s_dW

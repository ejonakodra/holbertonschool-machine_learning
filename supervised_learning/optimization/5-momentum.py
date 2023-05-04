#!/usr/bin/env python3
"""Function that updates a variable using gradient descent
with momentum optimization algorithm"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """Updates a variable using gradient descent
    with momentum optimization algorithm"""
    dW_prev = (beta1 * v) + ((1 - beta1) * grad)
    var -= (alpha * dW_prev)
    return var, dW_prev

#!/usr/bin/env python3
"""Function that creates the training op
for a neural network in TensorFlow using
the gradient descent with momentum optimization algorithm"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """Creates the training operation for a neural network in TensorFlow
    using the gradient descent with momentum optimization algorithm """
    dW_prev = (beta1 * v) + ((1 - beta1) * grad)
    var -= (alpha * dW_prev)
    return var, dW_prev

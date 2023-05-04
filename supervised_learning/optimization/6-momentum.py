#!/usr/bin/env python3
"""Function that creates the training op
for a neural network in TensorFlow using
the gradient descent with momentum optimization algorithm"""


import tensorflow as tf

def create_momentum_op(loss, alpha, beta1):
    """Creates the training operation for a neural network in TensorFlow
    using the gradient descent with momentum optimization algorithm """
    op = tf.train.MomentumOptimizer(alpha, beta1).minimize(loss)
    return op

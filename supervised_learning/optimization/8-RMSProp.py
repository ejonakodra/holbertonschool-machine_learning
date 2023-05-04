#!/usr/bin/env python3
"""Function creates the training op for a neural network in TensorFlow using
the RMSProp optimization algorithm"""



def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """Creates the training operation for a neural network in TensorFlow
    using the RMSProp optimization algorithm"""
    optimizer = tf.train.RMSPropOptimizer(learning_rate=alpha,
                                          decay=beta2, epsilon=epsilon)
    train_op = optimizer.minimize(loss)
    return train_op

#!/usr/bin/env python3
"""Function performes same convolution on a grayscale image"""


import numpy as np


def convolve_grayscale_same(images, kernel):
    """Performes a same convolution on a grayscale image,
    m: nr of img, h: height of imgs in pixels, w: width of imgs in pixels"""
    m, height, width = images.shape
    kh, kw = kernel.shape
    if (kh % 2) == 1 and (kw % 2) == 1:
        ph = (kh - 1) // 2
        pw = (kw - 1) // 2
    else:
        ph = kh // 2
        pw = kw // 2
    images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)),
                    'constant', constant_values=0)
    convoluted = np.zeros((m, height, width))
    for h in range(height):
        for w in range(width):
            output = np.sum(images[:, h: h + kh, w: w + kw] * kernel,
                            axis=1).sum(axis=1)
            convoluted[:, h, w] = output
    return convoluted

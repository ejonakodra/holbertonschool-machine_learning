#!/usr/bin/env python3
""" Poisson class represents Poisson distribution """


class Exponential:
    """ Exponencial class represents Exponencial distribution"""
    def __init__(self, data=None, lambtha=1.):
        """initialize lambda, as 1/mean in exp disttribution """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                lambtha = float(len(data) / sum(data))
                self.lambtha = lambtha

    def pdf(self, x):
        """calculates the value of the PMF"""
        if x < 0:
            return 0
        e = 2.7182818285
        pdf = self.lambtha * (e**(-self.lambtha*x))
        return pdf

    def cdf(self, x):
        """ calculates the value of the CDF"""
        if x < 0:
            return 0
        e = 2.7182818285
        cdf = 1 - (e**(-self.lambtha*x))
        return cdf

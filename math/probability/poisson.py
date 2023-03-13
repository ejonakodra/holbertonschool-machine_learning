#!/usr/bin/env python3
""" Poisson class represents Poisson distribution """


class Poisson:
    """    class that represents Poisson distribution """

    def __init__(self, data=None, lambtha=1.):
        """initialize lambda, 
        if data is given use the lambtha is it is positive
        if is not given, validate data and calculate lambtha """
        if data is None:
            if lambtha < 1:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                lambtha = float(sum(data) / len(data))
                self.lambtha = lambtha

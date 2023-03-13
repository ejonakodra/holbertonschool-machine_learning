#!/usr/bin/env python3
""" Normal class represents Normal distribution """


class Normal:
    """ Normal class represents Normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """initialize lambda, as 1/mean in exp disttribution """
        if data is None:
            if stddev < 1:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
                self.mean = float(mean)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = float(sum(data) / len(data))
                self.mean = mean
                sum_data = 0
                for i in data:
                    sum_data += ((i - mean) ** 2)
                stddev = (sum_data / len(data)) ** (1 / 2)
                self.stddev = stddev

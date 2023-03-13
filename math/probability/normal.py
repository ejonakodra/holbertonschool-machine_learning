#!/usr/bin/env python3
""" Normal class represents Normal distribution """


class Normal:
    """ Normal class represents Normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """initialize lambda, as 1/mean in exp disttribution """
        if data is None:
            if stddev < 1:
                raise TypeError("stddev must be a positive value")
            else:
                self.mean = float(mean)
                self.stddev = float(stddev)
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
                    sum_data += float((i - self.mean) ** 2)
                    self.stddev = sum_data/len(data)

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

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        mean = self.mean
        stddev = self.stddev
        z = (x - mean) / stddev
        return z

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        mean = self.mean
        stddev = self.stddev
        x = stddev * z + mean
        return x

    def pdf(self, x):
        """calculates the value of the PDF for a given x-value"""
        mean = self.mean
        stddev = self.stddev
        e = 2.7182818285
        pi = 3.1415926536
        power_e = e ** (-(1 / 2) * (self.z_score(x) ** 2))
        coefficient = 1 / (stddev * ((2 * pi) ** (1 / 2)))
        pdf = coefficient * power_e
        return pdf

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value"""
        mean = self.mean
        stddev = self.stddev
        pi = 3.1415926536
        value = (x - mean) / (stddev * (2 ** (1 / 2)))
        erf = value - ((value ** 3) / 3) + ((value ** 5) / 10)
        erf = erf - ((value ** 7) / 42) + ((value ** 9) / 216)
        erf *= (2 / (pi ** (1 / 2)))
        cdf = (1 / 2) * (1 + erf)
        return cdf

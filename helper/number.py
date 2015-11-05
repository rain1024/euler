__author__ = 'rain'

import math


def nCr(n, r):
    """
    :param n: int
    :param r: int
    :return: number of r-combination of a set length n
    """
    f = math.factorial
    return f(n) / f(r) / f(n - r)

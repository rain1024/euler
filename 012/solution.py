import timeit
from helper.prime import factors

__author__ = 'rain'


def triangular_number(n):
    return n * (n + 1) / 2


def solve():
    num_factor = 0
    i = 1
    while num_factor < 500:
        N = triangular_number(i)
        num_factor = len(factors(N))
        i += 1
    return N

print solve()

print timeit.timeit(solve, number=10)

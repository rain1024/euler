import timeit
import math

__author__ = 'rain'


def sum_of_squares(n):
    return (n * (n + 1) * (2*n + 1)) * 1.0 / 6

def square_of_sum(n):
    return math.pow(n, 2) * math.pow(n+1, 2) * 1.0 / 4

def diff(n):
    return square_of_sum(n) - sum_of_squares(n)

def solve():
    return format(diff(100), "30f")

print solve()

print timeit.timeit(solve, number=10)

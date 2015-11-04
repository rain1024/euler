from fractions import gcd
import timeit

__author__ = 'rain'

def lcm(a, b):
    return a * b / gcd(a, b)

def solve():
    n = 20
    smallest_multiple = 1
    for i in range(1, n+1):
        smallest_multiple = lcm(smallest_multiple, i)
    return smallest_multiple

print solve()

print timeit.timeit(solve, number=10)


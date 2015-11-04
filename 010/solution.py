import timeit
import re
from helper.prime import atkin
__author__ = 'rain'

def solve():
    primes = atkin(int(2e6))
    value = reduce(lambda x, y: x + y, primes, 0)
    return value

print solve()

print timeit.timeit(solve, number=10)

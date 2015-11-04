import timeit
import re

__author__ = 'rain'

def solve():
    for a in range(1, 500):
        for b in range(1, 500):
            for c in range(1, 500):
                if(a + b + c == 1000) and (a*a + b*b == c*c):
                    return a * b * c

print solve()

print timeit.timeit(solve, number=10)

import timeit
from helper import number

__author__ = 'rain'


def solve():
    N = 20
    return number.nCr(40, 20)

if __name__ == '__main__':
    print solve()
    print timeit.timeit(solve, number=10)

import timeit
import math

__author__ = 'rain'


def count_total_of_digit(number):
    return reduce(lambda x, y: str(int(x) + int(y)), number)


def solve():
    number = "%d" % math.pow(2, 1000)
    return count_total_of_digit(number)

if __name__ == '__main__':
    print solve()
    print timeit.timeit(solve, number=10)

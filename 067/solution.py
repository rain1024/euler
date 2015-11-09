__author__ = 'rain'

import timeit
from itertools import imap


def get_node_label(i, j):
    return str(i) + "." + str(j)


def solve():
    f = lambda above, below, below_shift: above + max(below, below_shift)
    find_max_local = lambda below, above: list(imap(f, above, below, below[1:]))
    data = [map(int, row.split()) for row in open("p067_triangle.txt")][::-1]
    return reduce(find_max_local, data)[0]


if __name__ == '__main__':
    print solve()
    print timeit.timeit(solve, number=10)

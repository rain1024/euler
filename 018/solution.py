__author__ = 'rain'

import timeit


def get_node_label(i, j):
    return str(i) + "." + str(j)


def find_max_local(x, y):
    return map(lambda i: max(x[i], x[i + 1]) + y[i], range(len(y)))


def solve():
    from itertools import imap
    data = [map(int, row.split()) for row in open("triangle.txt")][::-1]
    return reduce(find_max_local, data)[0]


if __name__ == '__main__':
    print solve()
    print timeit.timeit(solve, number=10)

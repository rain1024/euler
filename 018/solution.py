import timeit

__author__ = 'rain'


def get_node_label(i, j):
    return str(i) + "." + str(j)


def solve():
    from itertools import imap

    f = lambda x, y, z: x + max(y, z)
    g = lambda xs, ys: list(imap(f, ys, xs, xs[1:]))
    data = [map(int, row.split()) for row in open("triangle.txt")][::-1]
    return reduce(g, data)[0]


if __name__ == '__main__':
    print solve()
    print timeit.timeit(solve, number=10)

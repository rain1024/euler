import timeit
import inflect
__author__ = 'rain'


def solve():
    total = 0
    N = 1000
    for i in range(1, N+1):
        word = inflect.engine().number_to_words(i)
        word = word\
            .replace(" ", "")\
            .replace("-", "")
        total += len(word)
    return total

if __name__ == '__main__':
    print solve()
    print timeit.timeit(solve, number=10)

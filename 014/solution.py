import timeit

__author__ = 'rain'

# collatz sequence(n):
sequences = {}


def collatz_tranform(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

current = 1


def generate_sequence(initial_value):
    sequence = [initial_value]
    value = initial_value
    while value != 1:
        if sequences.has_key(value):
            sequence += sequences[value][1:]
            break
        else:
            next = collatz_tranform(value)
            sequence.append(next)
            value = next
    sequences[initial_value] = sequence
    return sequence


def solve():
    for i in range(1, int(100)):
        generate_sequence(i)
    longest_sequence = reduce(lambda x, y: x if len(x[1]) > len(y[1]) else y, enumerate(sequences.values()))
    print longest_sequence[0] + 1, ": ", longest_sequence[1]


if __name__ == '__main__':
    pass
    # print solve()
    #
    # print timeit.timeit(solve, number=0)

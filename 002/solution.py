import timeit

__author__ = 'rain'


def solve():
    max = 4e6
    count = 0
    fibonaci_number_1 = 1
    fibonaci_number_2 = 2
    while fibonaci_number_2 < max:
        if fibonaci_number_2 % 2 == 0:
            count += fibonaci_number_2
        temp = fibonaci_number_2
        fibonaci_number_2 += fibonaci_number_1
        fibonaci_number_1 = temp
    return count


print solve()
print timeit.timeit(solve, number=10)


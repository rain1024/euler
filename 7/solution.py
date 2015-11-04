import timeit
import math

__author__ = 'rain'


primes = [2]

def is_prime(n):
    for prime in primes:
        if n % prime == 0:
            return False
    return True


def find_nth_prime(n):
    current_index = 0
    while(len(primes) < n):
        if current_index == 0:
            start_value = 3
            end_value = 2 * 2
        else:
            start_value = primes[current_index - 1] * primes[current_index - 1] + 1
            end_value = primes[current_index] * primes[current_index]
        for i in range(start_value, end_value):
            if is_prime(i):
                primes.append(i)
        current_index += 1
    return primes[n-1]


def solve():
    return find_nth_prime(10001)

print solve()

print timeit.timeit(solve, number=10)

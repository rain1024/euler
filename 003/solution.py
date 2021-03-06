from math import sqrt, ceil
import timeit

__author__ = 'rain'
from SieveOfAtkin import atkin

def find_large_prime_factor(n):
    primes = atkin(int(sqrt(n)))
    for i in range(1, len(primes)):
        prime = primes[-i]
        if n % prime == 0:
            return prime
    return 1

def solve():
    return find_large_prime_factor(600851475143)

print solve()
print timeit.timeit(solve, number=10)


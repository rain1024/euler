import timeit

__author__ = 'rain'

def is_palindrome(n):
    number_in_string = str(n)
    return number_in_string == number_in_string[::-1]

def solve():
    max = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            if product > max and is_palindrome(product):
                max = product
    return max


print solve()

print timeit.timeit(solve, number=10)

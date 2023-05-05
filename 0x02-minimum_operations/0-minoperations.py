#!/usr/bin/python3
"""technical interview
"""
import math


def minOperations(n):
    """ a function to find minimum operations on a number
    """
    if n is None or n < 2:
        return 0
    prime_factors = []
    sum = 0

    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n / i

    if n > 2:
        prime_factors.append(n)

    for i in prime_factors:
        sum += i

    return int(sum)

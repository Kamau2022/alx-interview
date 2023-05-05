#!/usr/bin/python3
"""technical interview
"""
import math


def minOperations(n):
    """ a function to find minimum operations on a number
    """
    if type(n) != int or n <= 1:
        return 0
    numbers = []
    sum = 0

    while n % 2 == 0:
        numbers.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            numbers.append(i)
            n = n / i

    if n > 2:
        numbers.append(n)

    for i in numbers:
        sum += i

    return int(sum)

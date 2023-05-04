#!/usr/bin/python3
"""technical interview
"""


def minOperations(n):
    """a function to find the minimum operation
    """

    sum = 0
    i = 0
    p = 1
    for i in range(1, n + 1):
        k = p * 2
        p = p + 1
        sum = k + p
        if sum >= n:
            break
    return i + 3

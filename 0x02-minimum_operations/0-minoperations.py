#!/usr/bin/python3
"""technical interview
"""


def minOperations(n):
    """a function to find the minimum operation
    """

    sum = 1
    i = 0
    for i in range(1, n + 1):
        sum = sum + 2
        if sum == 9:
            sum = 9 + 3
            continue
        if sum == 6:
            sum = sum + 3
            continue
        if sum >= n:
            break
    return i + 2

#!/usr/bin/python3
"""technical interview
"""
import sys


def minOperations(n):
    """a function to find the minimum operation
    """

    sum = 0
    for i in range(1, n + 1):
        sum = sum + 1
        if sum == 3:
            sum = 3 * 2
            continue
        if sum == 6:
            sum = sum + 3
            continue
        if sum >= n:
            break
    return i

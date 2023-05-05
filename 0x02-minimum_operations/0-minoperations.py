#!/usr/bin/python3
"""technical interview
"""


def minOperations(n):
    """a function to find the minimum operation
    """

    if n is not int:
        return 0

    paste = 0
    copy = 2
    while (copy <= n):
        if not (n % copy):
            n = int(n / copy)
            paste += copy
            copy = 1
        copy += 1
    return paste

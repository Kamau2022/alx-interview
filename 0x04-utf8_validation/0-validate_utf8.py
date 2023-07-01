#!/usr/bin/python3
"""technical-interview
"""

def validUTF8(data):
    """a function to validate a given data set
       represents a valid UTF-8 encoding.
    """
    bits = to_bits(data)
    for byte in bits:
        # single byte char
        if byte[0] == 0:
            continue

        # multi-byte character
        amount = sum(takewhile(bool, byte))
        if amount <= 1:
            return False
        if amount >= MAX_NUMBER_OF_ONES:
            return False

        for _ in range(amount - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True

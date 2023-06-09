#!/usr/bin/python3
"""technical-interview
"""
NUMBER_OF_BITS_PER_BYTE = 8
MAX_NUMBER_OF_ONES = 4


def validUTF8(data):
    """a function to validate a given data set
       represents a valid UTF-8 encoding.
    """
    index = 0
    while index < len(data):
        number = data[index] & (2 ** 7)
        number >>= (NUMBER_OF_BITS_PER_BYTE - 1)
        if number == 0:
            index += 1
            continue
        number_of_ones = 0
        while True:
            number = data[index] & (2 ** (7 - number_of_ones))
            number >>= (NUMBER_OF_BITS_PER_BYTE - number_of_ones - 1)
            if number == 1:
                number_of_ones += 1
            else:
                break
            if number_of_ones > MAX_NUMBER_OF_ONES:
                return False
        if number_of_ones == 1:
            return False
        index += 1
        if index >= len(data) or index >= (index + number_of_ones - 1):
            return False
        for i in range(index, index + number_of_ones - 1):
            number = data[i]
            number >>= (NUMBER_OF_BITS_PER_BYTE - 1)
            if number != 1:
                return False
            number >>= (NUMBER_OF_BITS_PER_BYTE - 1)
            if number != 0:
                return False
            index += 1
    return True

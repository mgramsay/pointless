#!/usr/bin/env python3

"""
A collection of functions to determine if an integer is even.
"""

# --- EARLY VERSIONS --- #

def isEven_1(number):
    # All even numbers end with either 2, 4, 6, 8 or 0.
    # So just extract the last digit and test if it's one of these.
    assert isinstance(number, int) or isinstance(number, str)
    numberString = str(number)
    lastDigit = numberString[-1]
    if lastDigit == "0" or \
       lastDigit == "2" or \
       lastDigit == "4" or \
       lastDigit == "6" or \
       lastDigit == "8":
        return True
    return False

def isEven_2(number):
    # Numbers alternate odd-even-odd. Assuming 0 is even,
    # can loop from 0 until we reach required number.
    assert isinstance(number, int) or isinstance(number, str)
    value = abs(int(number))
    isEven = False
    for n in range(0, value+1):
        isEven = not isEven
    return isEven


# --- FINAL VERSIONS --- #

def isEven(number):
    assert isinstance(number, int) or isinstance(number, str)
    value = abs(int(number))
    if value == 0:
        return True
    return not isEven(value-1)


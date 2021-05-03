#!/usr/bin/env python3

"""
A function to determine if an integer is odd.
"""

from isEven import isEven

def isOdd(number):
    # To test if a number is odd, can exploit the fact that
    # odd numbers aren't even.
    return not isEven(number)


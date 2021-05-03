#!/usr/bin/env python3

"""
Function to determine if a number is divisible by three
"""

def divisibleByThree(number):
    # If a number is divisible by three, the sum of its digits are too.
    # So keep summing digits until we get a number less than 10.
    # If that number is 3, 6 or 9, the original number was divisible by three.
    assert isinstance(number, int) or isinstance(number, str)
    numberString = str(abs(int(number)))
    if len(numberString) == 1:
        if numberString == "0" or \
           numberString == "3" or \
           numberString == "6" or \
           numberString == "9":
            return True
        return False
    else:
        digitSum = 0
        for n in numberString:
            digitSum += int(n)
        return divisibleByThree(digitSum)


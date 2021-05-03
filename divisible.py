#!/usr/bin/env python3

from isEven import isEven
from divideThree import divisibleByThree

def divisible(number, divisor):
    assert isinstance(number, int) or isinstance(number, str)
    assert isinstance(divisor, int) or isinstance(divisor, str)
    if int(divisor) == 2:
        return isEven(number)
    elif int(divisor) == 3:
        return divisibleByThree(number)
    elif int(divisor) == 5:
        numberString = str(abs(int(number)))
        lastDigit = numberString[-1]
        if lastDigit == "5" or lastDigit == "0":
            return True
        return False
    elif int(divisor) == 10:
        numberString = str(abs(int(number)))
        lastDigit = numberString[-1]
        if lastDigit == "0":
            return True
        return False
    else:
        if divisible(divisor, 2):
            return divisible(number, 2) and divisible(number//2, divisor//2)
        elif divisible(divisor, 3):
            return divisible(number, 3) and divisible(number//3, divisor//3)
        n = 0
        while n <= number:
            if n == number:
                return True
            n += divisor
        return False

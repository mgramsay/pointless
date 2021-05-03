#!/usr/bin/env python3

from isEven import isEven
from isOdd import isOdd
from divideThree import divisibleByThree
from divisible import divisible

print("Testing isEven")
# Check returns true if number is even
assert isEven(-2)
assert not isEven(-1)
assert isEven(0)
assert not isEven(1)
assert isEven(2)
assert not isEven(3)

# Check works with strings
assert isEven("-2")
assert not isEven("-1")
assert isEven("0")
assert not isEven("1")
assert isEven("2")
assert not isEven("3")

print("Testing isOdd")
# Check returns true if number is odd
assert not isOdd(-2)
assert isOdd(-1)
assert not isOdd(0)
assert isOdd(1)
assert not isOdd(2)
assert isOdd(3)

# Check works with strings
assert not isOdd("-2")
assert isOdd("-1")
assert not isOdd("0")
assert isOdd("1")
assert not isOdd("2")
assert isOdd("3")

print("Testing divisibleByThree")
assert divisibleByThree(3)
assert not divisibleByThree(4)
assert divisibleByThree(69)
assert not divisibleByThree(68)
assert divisibleByThree(-69)
assert not divisibleByThree(-68)

assert divisibleByThree("3")
assert not divisibleByThree("4")
assert divisibleByThree("69")
assert not divisibleByThree("68")
assert divisibleByThree("-69")
assert not divisibleByThree("-68")

print("All tests passed")

for j in range(1, 11):
    print("Divides by:", j)
    for i in range(0, 11):
        print(i, divisible(i, j))

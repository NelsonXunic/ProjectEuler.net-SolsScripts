# This is a script used to solve a problem from the bank of problems found in ProjectEuler.net
# https://projecteuler.net/archives
# Problem 5: Smallest Multiple
# The problem is as follows:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import  math

import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def find_smallest_multiple(n):
    smallest_multiple = 1
    for i in range(1, n + 1):
        smallest_multiple = lcm(smallest_multiple, i)
    return smallest_multiple

if __name__ == '__main__':
    print(find_smallest_multiple(100))
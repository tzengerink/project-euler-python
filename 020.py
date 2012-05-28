#!/usr/bin/env python2
"""
PROBLEM 20
----------
n! means n  (n  1)  ...  3  2  1
For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!

Copyright (c) Project Euler
See: http://projecteuler.net/copyright

SOLUTION
--------
648

Copyright (c) 2012, T. Zengerink
"""

from profiler import Profiler


def factorial(n):
    """Calculate the factorial for N."""
    t = 1
    for i in range(1, n + 1):
        t *= i
    return t


def sum_factorial(n):
    """Sum the digits in factorial N."""
    t = 0
    for i in str(factorial(n)):
        t += int(i)
    return t


if __name__ == "__main__":
    print(sum_factorial(100))
    Profiler.report()

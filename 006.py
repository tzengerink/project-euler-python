#!/usr/bin/env python2
"""
PROBLEM 6
---------
The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 + 385 = 2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

Copyright (c) Project Euler
See: http://projecteuler.net/copyright

SOLUTION
--------
25164150

Copyright (c) 2012, T. Zengerink
See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""

from profiler import Profiler


def range_sum_squares(begin, end):
    """Calculate the sum of all squares in a range."""
    t = 0
    for i in range(begin, end):
        t += i**2
    return t


def range_square_sums(begin, end):
    """Calculate the square of a summed range."""
    t = 0
    for i in range(begin, end):
        t += i
    return t**2


def range_square_sum_diff(begin, end):
    """
    Calculate the difference between the sum of squares and the square of
    sums.
    """
    return range_square_sums(begin, end) - range_sum_squares(begin, end)


if __name__ == "__main__":
    print(range_square_sum_diff(1, 101))
    Profiler.report()

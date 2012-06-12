#!/usr/bin/env python2
"""
PROBLEM 21
----------
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each
of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

Copyright (c) Project Euler
See: http://projecteuler.net/copyright

SOLUTION
--------
31626

Copyright (c) 2012, T. Zengerink
See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""

from profiler import Profiler
from math import floor


def d(n):
    """Sum all proper divors of N."""
    return sum(proper_divisors(n))


def proper_divisors(n):
    """Get a list of all proper divisors of N."""
    d, r = [], int(floor(n**.5))
    for i in range(1, r):
        if not n % i:
            d.extend([i, n / i])
    if not n**.5 % 1:
        d.append(n)
    return filter(lambda x: x != n, d)


def amicable_numbers(n):
    """Get all amicable numbers up to N."""
    a = []
    for i in range(1, n):
        result = d(i)
        if i != result and d(result) == i and i not in a:
            a.append(i)
    return a


if __name__ == "__main__":
    print(sum(amicable_numbers(10000)))
    Profiler.report()

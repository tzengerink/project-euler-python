#!/usr/bin/env python2
"""
PROBLEM 9
---------
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc

Copyright (c) Project Euler
See: http://projecteuler.net/copyright

SOLUTION
--------
31875000

Copyright (c) 2012, T. Zengerink
See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""

from profiler import Profiler


def product(l):
    """Get the product of the items in an iterable."""
    t = 1
    for i in l:
        t *= int(i)
    return t


def triplet(n):
    """Find the Pythagorean triplet who's sum equals a given number."""
    for c in range(n - 3, 1, -1):
        for b in range(c - 1, 1, -1):
            a = (c**2 - b**2)**.5
            if a + b + c == n:
                return [c, b, int(a)]
    return False


def triplet_product(n):
    """Find the product of a triplet, whos sum equals a given number."""
    t = triplet(n)
    if not t:
        raise Exception("Unable to find triplet")
    return product(t)


if __name__ == "__main__":
    print(triplet_product(1000))
    Profiler.report()

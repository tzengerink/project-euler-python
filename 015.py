#!/usr/bin/env python2
"""
PROBLEM 15
----------
Starting in the top left corner of a 2x2 grid, there are 6 routes (without
backtracking) to the bottom right corner.
How many routes are there through a 20x20 grid?

Copyright (c) Project Euler
See: http://projecteuler.net/copyright

SOLUTION
--------
137846528820

Copyright (c) 2012, T. Zengerink
"""

from profiler import Profiler


def factorial(n):
    """Calculate the factorial for N."""
    t = 1
    for i in range(1, n + 1):
        t *= i
    return t


def routes(s):
    """Calculate the number of routes for grid width given width and height."""
    return (factorial(s * 2) / factorial(s)) / factorial(s)


if __name__ == "__main__":
    print(routes(20))
    Profiler.report()

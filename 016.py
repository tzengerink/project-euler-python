#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    PROBLEM 16
    ----------
    2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2 ** 1000?

    Copyright (c) Project Euler
    See: http://projecteuler.net/copyright

    SOLUTION
    --------
    1366

    Copyright (c) 2012, T. Zengerink
    See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""
from profiler import Profiler


def sum_digits(n):
    """Sum the digits of N."""
    L = []
    for s in str(n):
        L.append(int(s))
    return sum(L)


if __name__ == "__main__":
    print(sum_digits(2**1000))
    Profiler.report()

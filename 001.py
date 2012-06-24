#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    PROBLEM 1
    ---------
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we
    get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.

    Copyright (c) Project Euler
    See: http://projecteuler.net/copyright

    SOLUTION
    --------
    233168

    Copyright (c) 2012, T. Zengerink
    See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""
from profiler import Profiler


def sum_multiples_of(a, b, n):
    """Get the sum of all multiples of A and B up to N."""
    total = 0
    for i in range(1, n):
        if not i % a or not i % b:
            total += i
    return total


if __name__ == "__main__":
    print(sum_multiples_of(3, 5, 1000))
    Profiler.report()

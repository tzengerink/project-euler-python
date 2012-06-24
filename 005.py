#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    PROBLEM 5
    ---------
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?

    Copyright (c) Project Euler
    See: http://projecteuler.net/copyright

    SOLUTION
    --------
    232792560

    Copyright (c) 2012, T. Zengerink
    See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""
from profiler import Profiler


def can_be_devided_by_list(n, l):
    """See if a number can be devided by all numbers in a list."""
    if n == 0:
        return False
    for i in l:
        if n % i:
            return False
    return True


def smallest_divisible_for_range(start, end):
    """Get the highest number that is divisible by all numbers in a range."""
    i = 0
    while not can_be_devided_by_list(i, range(end, start, -1)):
        i += end
    return i


if __name__ == "__main__":
    print(smallest_divisible_for_range(1, 20))
    Profiler.report()

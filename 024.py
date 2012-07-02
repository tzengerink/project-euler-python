#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    PROBLEM 24
    ----------
    A permutation is an ordered arrangement of objects. For example, 3124 is one
    possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
    are listed numerically or alphabetically, we call it lexicographic order.
    The lexicographic permutations of 0, 1 and 2 are:
        012   021   102   120   201   210
    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
    5, 6, 7, 8 and 9?

    Copyright (c) Project Euler
    See: http://projecteuler.net/copyright

    SOLUTION
    --------
    2783915460

    Copyright (c) 2012, T. Zengerink
    See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""
from profiler import Profiler
from itertools import permutations

if __name__ == "__main__":
    L = []
    for p in permutations("0123456789"):
        L.append("".join(p))
    print(L[1000000 - 1])
    Profiler.report()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    PROBLEM 25
    ----------
    The Fibonacci sequence is defined by the recurrence relation:
        Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
        F1 = 1
        F2 = 1
        F3 = 2
        F4 = 3
        F5 = 5
        F6 = 8
        F7 = 13
        F8 = 21
        F9 = 34
        F10 = 55
        F11 = 89
        F12 = 144
    The 12th term, F12, is the first term to contain three digits.
    What is the first term in the Fibonacci sequence to contain 1000 digits?

    Copyright (c) Project Euler
    See: http://projecteuler.net/copyright

    SOLUTION
    --------
    4782

    Copyright (c) 2012, T. Zengerink
    See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""
from profiler import Profiler


def fibonacci(n):
    """Get all terms of the Fibonacci sequence until the first term has a
    length of N digits."""
    a, b = 1, 1
    f = [a, b]
    while len(str(b)) < n:
        a, b = b, a + b
        f.append(b)
    return f


if __name__ == "__main__":
    print(len(fibonacci(1000)))
    Profiler.report()

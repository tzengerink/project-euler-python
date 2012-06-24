#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    PROBLEM 4
    ---------
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 99.
    Find the largest palindrome made from the product of two 3-digit numbers.

    Copyright (c) Project Euler
    See: http://projecteuler.net/copyright

    SOLUTION
    --------
    906609

    Copyright (c) 2012, T. Zengerink
    See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""
from profiler import Profiler


def is_palindrome(s):
    """Checks if a string is a palindrome."""
    s = str(s).lower()
    adjust = 0
    if (len(s) % 2):
        adjust = 1
    b = s[:(len(s) - adjust) / 2]
    e = s[(len(s)):(len(s) - 1) / 2:-1]
    return (b == e)


def highest_palindrome_product(x, y):
    """Get the highest palindrome product of a range."""
    p = []
    for i in range(x, y, -1):
        for j in range(x, y, -1):
            product = i * j
            if (is_palindrome(product)):
                p.append(product)
    return max(p)


if __name__ == "__main__":
    print(highest_palindrome_product(1000, 100))
    Profiler.report()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    PROBLEM 10
    ----------
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.

    Copyright (c) Project Euler
    See: http://projecteuler.net/copyright

    SOLUTION
    --------
    142913828922

    Copyright (c) 2012, T. Zengerink
    See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""
from profiler import Profiler


def is_prime(n):
    """See if a number is a prime number."""
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True


def sum_primes_lower_than(n):
    t = 0
    for i in range(2, n + 1):
        if is_prime(i):
            t += i
    return t


if __name__ == "__main__":
    print(sum_primes_lower_than(2000000))
    Profiler.report()

#!/usr/bin/env python2
"""
PROBLEM 3
---------
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Copyright (c) Project Euler
See: http://projecteuler.net/copyright

SOLUTION
--------
6857

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


def highest_prime_factor(n):
    """Get the highest prime factor of a number."""
    for i in range(int(n**0.5)+1, 1, -2):
        if not n % i and is_prime(i):
            return i


if __name__ == "__main__":
    print(highest_prime_factor(600851475143))
    Profiler.report()

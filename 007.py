#!/usr/bin/env python2
"""
PROBLEM 7
---------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.
What is the 10 001st prime number?

Copyright (c) Project Euler
See: http://projecteuler.net/copyright

SOLUTION
--------
104743

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


def next_prime(n):
    """Get the first prime number following a given number."""
    n += 1
    while not is_prime(n):
        n += 1
    return n


def prime_list(length):
    """Get a list of prime numbers with a given length."""
    l, i = [], 1
    while len(l) < length:
        i = next_prime(i)
        l.append(i)
    return l


if __name__ == "__main__":
    print(prime_list(10001).pop())
    Profiler.report()

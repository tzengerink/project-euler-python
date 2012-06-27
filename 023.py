#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    PROBLEM 23
    ----------
    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors of
    28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number. A number n is called deficient if the sum of its proper divisors is
    less than n and it is called abundant if this sum exceeds n.
    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
    number that can be written as the sum of two abundant numbers is 24. By
    mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers. However, this upper limit
    cannot be reduced any further by analysis even though it is known that the
    greatest number that cannot be expressed as the sum of two abundant numbers
    is less than this limit.
    Find the sum of all the positive integers which cannot be written as the sum
    of two abundant numbers.

    Copyright (c) Project Euler
    See: http://projecteuler.net/copyright

    SOLUTION
    --------
    4179871

    Copyright (c) 2012, T. Zengerink
    See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""
from profiler import Profiler
from math import floor


class Abundant():
    """Assist in calculations concerning abundant numbers."""
    def __init__(self, top):
        self.top = top
        self.numbers = set([x for x in range(1, self.top + 1)
            if self.is_abundant(x)])

    def is_abundant(self, n):
        """Check if a number is an abundant number."""
        return sum(self.proper_divisors(n)) > n

    def is_pair(self, n):
        """Check if a number is the sum of two abundant numbers."""
        for x, y in self.parts(n):
            if x in self.numbers and y in self.numbers:
                return True
        return False

    def non_pairs(self):
        """Get a list of numbers not the sum of two abundant numbers."""
        return [x for x in range(1, self.top + 1) if not self.is_pair(x)]

    def parts(self, n):
       """Get a list of all numeric pairs that sum to N."""
       return [(x, n - x) for x in range(1, int(floor(n / 2) + 1))]

    def proper_divisors(self, n):
        """Get a list of all proper divisors of N."""
        d, r = [], int(floor(n ** .5) + 1)
        for i in range(1, r):
            if not n % i and i not in d:
                d.extend([i, n / i])
        if not n ** .5 % 1:
            d.append(n)
        d = set(d)
        if n in d:
            d.remove(n)
        return list(d)


if __name__ == "__main__":
    A = Abundant(20161)
    print(sum(A.non_pairs()))
    Profiler.report()

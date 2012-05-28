#!/usr/bin/env python2
"""
PROBLEM 14
----------
The following iterative sequence is defined for the set of positive integers:
    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
    13 ->  40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

Copyright (c) Project Euler
See: http://projecteuler.net/copyright

SOLUTION
--------
837799

Copyright (c) 2012, T. Zengerink
See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""

from profiler import Profiler


class Collatz:
    """Responsible for calculations concerning Collatz chains."""
    def __init__(self):
        self.chains = {}

    def calculate_chain_length(self, n):
        """Calculate the Collatz chain length for N."""
        c = 1
        while n >= 2:
            n = (n * 3) + 1 if n % 2 else n / 2
            if n in self.chains:
                c += self.chains[n]
                break
            c += 1
        return c

    def chain_length(self, n):
        """Get a length of the Collatz chain for N."""
        if n not in self.chains:
            self.chains[n] = self.calculate_chain_length(n)
        return self.chains[n]

    def longest_chain(self, n):
        """Get the longest chain for numbers lower than N."""
        m = (0, 0)
        for i in range(1, n):
            if self.chain_length(i) >= m[1]:
                m = (i, self.chain_length(i))
        return m[0]


if __name__ == "__main__":
    c = Collatz()
    print(c.longest_chain(1000000))
    Profiler.report()

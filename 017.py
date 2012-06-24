#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    PROBLEM 17
    ----------
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?
    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
    letters. The use of "and" when writing out numbers is in compliance with
    British usage.

    Copyright (c) Project Euler
    See: http://projecteuler.net/copyright

    SOLUTION
    --------
    21124

    Copyright (c) 2012, T. Zengerink
    See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""
from profiler import Profiler

class Numbers:
    """Helps calculating the number of characters needed to spell a number."""

    # List of numbers
    nums = [1000, 100, 90, 80, 70, 60, 50, 40, 30, 20, 19, 18, 17, 16, 15,
            14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # Written numbers
    num_strings = {
        1   : "one",
        2   : "two",
        3   : "three",
        4   : "four",
        5   : "five",
        6   : "six",
        7   : "seven",
        8   : "eight",
        9   : "nine",
        10  : "ten",
        11  : "eleven",
        12  : "twelve",
        13  : "thirteen",
        14  : "fourteen",
        15  : "fifteen",
        16  : "sixteen",
        17  : "seventeen",
        18  : "eighteen",
        19  : "nineteen",
        20  : "twenty",
        30  : "thirty",
        40  : "forty",
        50  : "fifty",
        60  : "sixty",
        70  : "seventy",
        80  : "eighty",
        90  : "ninety",
        100 : "hundred",
        1000: "thousand",
    }

    # Character counts
    char_counts = {}

    def __init__(self):
        self.count_chars()

    def count_chars(self):
        """Count the number of chars in each number."""
        for n, c in self.num_strings.iteritems():
            self.char_counts[n] = len(c)
        self.char_counts['and'] = 3

    def numbers(self, n):
        """Get a list of tuples for numbers in N."""
        L = []
        while n >= 1:
            for i in self.nums:
                if n % i != n:
                    L.append((i, n / i))
                    if i == 100 and n % i:
                        L.append(('and', 1))
                    n = n % i
        return L

    def chars(self, n):
        """Get the number of chars for N."""
        t = 0
        for i, c in self.numbers(n):
            t += self.char_counts[i]
            if i == 100 or i == 1000:
                t += self.char_counts[c]
        return t

    def sum_chars(self, n):
        """Sum the number of chars up to N."""
        t = 0
        for i in range(1, n + 1):
            t += self.chars(i)
        return t


if __name__ == "__main__":
    n = Numbers()
    print(n.sum_chars(1000))
    Profiler.report()

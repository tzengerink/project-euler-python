#!/usr/bin/env python2
"""
PROBLEM 19
----------
You are given the following information, but you may prefer to do some research
for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

Copyright (c) Project Euler
See: http://projecteuler.net/copyright

SOLUTION
--------
171

Copyright (c) 2012, T. Zengerink
"""

from profiler import Profiler


def days_in_month(m, y):
    """
    Get the number of days in a month.
    m -- Month as a number
    y -- Year (YYYY)
    """
    if m in [4, 6, 9, 11]:
        return 30
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if not y % 400 or not y % 4 and y % 100:
        return 29
    return 28


def days_in_year(y):
    """
    Get the number of days in a year.
    y -- Year (YYYY)
    """
    if not y % 400 or not y % 4 and y % 100:
        return 366
    return 365


def sundays_on_first(f, y):
    """
    Get the numbers of sundays that fell on the first of a month.
    f -- First day of the year (1 = Monday, 7 = Sunday)
    y -- Year (YYYY)
    """
    m, sundays = 1, 0
    while m <= 12:
        if f in [0, 7]:
            sundays += 1
        f = (f + days_in_month(m, y)) % 7
        m += 1
    return sundays


def sundays_on_first_in_century(f=2, c=20):
    """
    Get the number of sundays on the first of the month for an entire century.
    f -- First day of the century (1 = Monday, 7 = Sunday)
    c -- Century (default = 20)
    """
    sundays = 0
    for y in range(((c - 1) * 100) + 1, c * 100 + 1):
        sundays += sundays_on_first(f, y)
        f = (f + days_in_year(y)) % 7
        if f == 0:
            f = 7
    return sundays


if __name__ == "__main__":
    print(sundays_on_first_in_century())
    Profiler.report()

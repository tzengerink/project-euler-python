#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    PROBLEM 22
    ----------
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
    containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.
    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
    would obtain a score of 938  53 = 49714.
    What is the total of all the name scores in the file?

    Copyright (c) Project Euler
    See: http://projecteuler.net/copyright

    SOLUTION
    --------
    871198282

    Copyright (c) 2012, T. Zengerink
    See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""
from profiler import Profiler


def sort_file(f):
    """Create sorted list of names from file contents."""
    handle = open(f, 'r')
    return sorted(handle.read().replace('\"', '').split(','))


def alphabet_values(L):
    """Create a list containing all alphabet values of the words in L."""
    alphabet = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9,
        'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18,
        's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26 }
    values = []
    for word in L:
        val = 0
        for char in word.lower():
           val += alphabet[char]
        values.append(val)
    return values


def scores(L):
    """Get the scores (position * alphabet score) for all words in list."""
    scores = []
    for key, val in enumerate(L):
        scores.append(val * (key + 1))
    return scores


if __name__ == "__main__":
    print(sum(scores(alphabet_values(sort_file('./data/022.txt')))))
    Profiler.report()

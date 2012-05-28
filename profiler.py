#!/usr/bin/env python
"""
Copyright (c) 2012, T. Zengerink
See: https://raw.github.com/Mytho/project-euler-python/master/LISENCE
"""

import time


class Profiler:
    """
    Profile the execution of an algoritm. Example usage:
    >>> Profiler.start()
    >>> [(x + 10) for x in range(10)]
    >>> Profiler.report()
    """

    # Start time
    begin = 0

    # End time
    end = 0

    @staticmethod
    def start():
        """Register the start time if not yet set, and return it."""
        if not Profiler.begin:
            Profiler.begin = time.time()
        return Profiler.begin

    @staticmethod
    def stop():
        """Register the stop time if not yet set, and return it."""
        if not Profiler.end:
            Profiler.end = time.time()
        return Profiler.end

    @staticmethod
    def report():
        """Print report off the time of execution."""
        diff = (Profiler.stop() - Profiler.start())
        print("- - -")
        print("It took %.6f seconds to run" % diff)


if __name__ != "__main__":
    """Register the start time whenever the profiler code is imported."""
    Profiler.start()

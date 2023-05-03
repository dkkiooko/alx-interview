#!/usr/bin/python3
""" find minimum operations"""


def minOperations(n):
    """ find minimum number of operations """
    minimum = 2
    total = 0
    while n > 1:
        while n % minimum == 0:
            total += minimum
            n /= minimum
        minimum += 1
    return total

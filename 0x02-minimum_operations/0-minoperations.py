#!/usr/bin/env python3
""" find minimum operations"""


def minOperations(n):
    """ find minimum number of operations """
    if (n == 1):
        return 0
    if (n == 2):
        return 2
    count = 'HH'
    operations = 2
    paste = 'H'
    while operations <= n:
        if (n % len(count) == 0):
            operations = operations + 2
            paste = paste + paste
            count = count + paste
        else:
            operations = operations + 1
            count = count + paste
        if len(count) == n:
            return operations

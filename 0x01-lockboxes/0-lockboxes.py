#!/usr/bin/python3
""" lock boxes
"""


def canUnlockAll(boxes):
    """ checks if all the boxes can be unlocked
    """
    n = len(boxes)
    seen = set([0])
    unseen = set(boxes[0])
    while len(unseen) > 0:
        index = unseen.pop()
        if not index or index >= n:
            continue
        if index not in seen:
            unseen = unseen.union(boxes[index])
            seen.add(index)
    return n == len(seen)

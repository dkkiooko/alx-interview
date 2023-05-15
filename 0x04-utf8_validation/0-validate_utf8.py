#!/usr/bin/python3
""" validate whether data set is a valid UTF-8 encoding """
from typing import List


def validUTF8(data: List[int]) -> bool:
    """validates whether data set is valid UTF-8

    Args:
        data (List[int]): _list of integers_

    Returns:
        bool: _whether data is vaild or not_
    """
    # number of bytes in UTF-8 character
    n_bytes = 0

    # mask to check if MSB is active
    mask1 = 1 << 7

    # mask to check if 2nd MSB is active
    mask2 = 1 << 6

    for num in data:
        # for first byte(s) check number of active MSBs
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
            if n_bytes == 0:
                # 1 byte characters
                continue
            if n_bytes == 1 or n_bytes > 4:
                # invalid scenario if 1, then not valid
                # if larger than 4, then invalid utf-8 coz max is 4
                return False
        else:
            # look at the 2 MSBs make sure its 10
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0

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
    count = 0

    for num in data:
        # loop through to check whether dataset complies
        if count == 0:
            # if first code point, there can be multiple bytes starting with 0
            if num & 128 == 0:
                count = 0
            elif num & 224 == 192:
                # if second code point, MSB must be 11
                count = 1
            elif num & 240 == 224:
                # if 3rd code point, MSB must be 111
                count = 2
            elif num & 248 == 240:
                # 4th code point, MSB Must be 1111
                count = 3
            else:
                # no other valid utf-8 encoding
                return False
        else:
            if num & 192 != 128:
                # if not first byte, MSB must be 10
                return False
            # reduce count to appropriate number of bytes
            count -= 1
        if count == 0:
            return True
        return False

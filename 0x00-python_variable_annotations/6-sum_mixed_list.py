#!/usr/bin/env python3

"""
Function takes a list of integers and floats and returns their sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Parameters
        mxd_list: List[Union[int, float]]

    Return
        sum of the list as a float
    """

    return sum(mxd_list)

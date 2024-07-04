#!/usr/bin/env python3

"""
Function takes a string and an int OR float as arguments and returns a tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Parameters
        k: str
        v: Union[int, float]

    Return
        tuple with k and v*v
    """

    return (k, v ** 2)

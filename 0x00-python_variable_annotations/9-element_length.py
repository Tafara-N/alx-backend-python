#!/usr/bin/env python3

"""
Function that takes a list of strings and returns a list of tuples
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Parameters
        lst : Iterable[Sequence]

    Return
        A list of tuples
    """

    return [(i, len(i)) for i in lst]

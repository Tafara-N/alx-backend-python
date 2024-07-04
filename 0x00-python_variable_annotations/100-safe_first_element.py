#!/usr/bin/env python3

"""
Function that returns the first element of a list, otherwise None if empty
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Parameters:
        lst (Sequence): A sequence of elements

    Return
        Union[Any, None]: First element of the sequence or None if empty
    """

    if lst:
        return lst[0]
    else:
        return None

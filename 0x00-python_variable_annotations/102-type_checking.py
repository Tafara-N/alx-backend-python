#!/usr/bin/env python3

"""
Function that zooms an array
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Parameters:
        lst (Tuple): The tuple of elements to be zoomed in
        factor (int, optional): The number of times each element in the tuple
                    should be repeated in the resulting list. Defaults to 2.

    Returns:
        A list of elements of the input tuple, each repeated `factor` times
    """

    zoomed_in: List = [
        item for item in lst for i in range(factor)
        ]

    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))

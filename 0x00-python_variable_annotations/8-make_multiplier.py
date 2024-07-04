#!/usr/bin/env python3

"""
Function takes a float as argument and returns a function that multiplies
a float by `multiplier`
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Parameters
        multiplier: float

    Return
        function that multiplies a float by `multiplier`
    """

    def multiply(number: float) -> float:
        """
        Parameters
            number: float

        Return
            nuumber * multiplier
        """

        return number * multiplier

    return multiply

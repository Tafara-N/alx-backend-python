#!/usr/bin/env python3

"""
A coroutine that collects 10 random numbers using an async comprehensing over
`async_generator`, then returns the 10 random numbers
"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Return
        A list of 10 random numbers
    """

    return [
        numbers async for numbers in async_generator()
    ]

#!/usr/bin/env python3

"""
Function waits for a random delay between 0 and `max_delay` (included and float
 value) seconds and eventually returns it.
"""

import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Parameters
        max_delay: int, default 10

    Return
        float(value): random delay between 0 and `max_delay` seconds
    """

    wait_time = max_delay * random()
    await asyncio.sleep(wait_time)
    return wait_time


if __name__ == "__main__":
    asyncio.run(wait_random())

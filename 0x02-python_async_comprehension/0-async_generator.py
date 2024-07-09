#!/usr/bin/env python3

"""
A coroutine that loops 10 times, each time asynchronously waits 1 second, then
yields a random number between 0 and 10 using the random module.
"""

import asyncio
import random

from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """
    Yield
        Random numbers between 0 and 10
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()  # type: ignore

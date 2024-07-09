#!/usr/bin/env python3

"""
A coroutine that executes `async_comprehension` four times in parallel using
`asyncio.gather` and measures the total runtime and returns it
"""

import asyncio
import time

async_comprehension = __import__(
    "1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Return
        The total runtime
    """

    started: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    finished: float = time.perf_counter()

    return finished - started

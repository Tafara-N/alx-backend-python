#!/usr/bin/env python3

"""
Function takes an integer `max_delay` and returns a `asyncio.Task`
"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """

    """

    tasks = [
        asyncio.create_task(wait_random(max_delay)) for _ in range(n)
    ]

    return [
        await task for task in asyncio.as_completed(tasks)
    ]


if __name__ == "__main__":
    asyncio.run(task_wait_n(5, 5))

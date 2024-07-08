#!/usr/bin/env python3

"""
Function measures the total execution time for `wait_n(n, max_delay`) and
returns a float `total_time / n`
"""


import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Parameters
        n: int
        max_delay: float

    Return
        A float: total_time / n
    """

    started = time.time()
    asyncio.run(wait_n(n, max_delay))
    finished = time.time()

    return (finished - started) / n


if __name__ == "__main__":
    measure_time(5, 5)

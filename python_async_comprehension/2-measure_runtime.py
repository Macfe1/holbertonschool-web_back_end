#!/usr/bin/env python3
"""
This module execute the async_comprehension corutine
function four times and measure the runtime it takes
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times concurrently using asyncio.gather.

    This function records the start time, runs four instances
    of async_comprehension concurrently, and then calculates
    the total elapsed time.

    Returns:
        float: The total execution time in seconds.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    total_time = end - start
    return total_time

"""
This module provides an asynchronous function to introduce
a random delay before returning its value.
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronously waits for a random delay and returns the delay time.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The actual delay time in seconds.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

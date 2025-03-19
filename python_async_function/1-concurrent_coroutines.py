#!/usr/bin/env python3
"""
This module provides a function corutine that use
the wait_random function n times
"""

from typing import List
import asyncio
wait_random_func = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes the wait_random coroutine `n` times with a given `max_delay`
    and returns a list of all delays in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay value for wait_random.

    Returns:
        List[float]: A list of delay values in ascending order.
    """
    corutineList = [wait_random_func(max_delay) for _ in range(n)]

    delaysList = sorted(await asyncio.gather(*corutineList))
    return delaysList

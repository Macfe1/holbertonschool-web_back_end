#!/usr/bin/env python3
"""
This module provides an asynchronous generator function that
yields a random float between 0 and 10, ten times, with a
1-second delay between each yield.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields a random float between
    0 and 10, ten times, with a 1-second delay between each yield.

    Yields:
        float: A randomly generated number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

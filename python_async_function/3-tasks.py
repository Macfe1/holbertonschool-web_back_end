#!/usr/bin/env python3
"""
This module provides a function to create an asyncio.Task
from the wait_random coroutine.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task
    for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay
        in seconds for wait_random.

    Returns:
        asyncio.Task: A task that runs wait_random with the given delay.
    """

    task = asyncio.create_task(wait_random(max_delay))
    return task

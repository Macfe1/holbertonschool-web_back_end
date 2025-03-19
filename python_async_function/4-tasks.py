#!/usr/bin/env python3
"""
This module provides an asynchronous function to execute multiple
tasks concurrently using asyncio.
"""

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple instances of task_wait_random concurrently.

    Args:
        n (int): Number of tasks to create.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: A sorted list of delays from all completed tasks.
    """

    taskList = [task_wait_random(max_delay) for _ in range(n)]

    delaysList = sorted(await asyncio.gather(*taskList))

    return delaysList

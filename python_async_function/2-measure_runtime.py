#!/usr/bin/env python3
"""
This module provides a function to measure the average execution time
of the asynchronous function wait_n.
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of wait_n
    and returns the average time per call.

    Args:
        n (int): Number of times wait_n should be executed.
        max_delay (int): Maximum delay value for wait_n.

    Returns:
        float: The average execution time per coroutine call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n

#!/usr/bin/env python3
"""
This module provides a function that takes a float
and rounds it down to the nearest integer.
"""
import math


def floor(n: float) -> int:
    """
    Take a float and rounds it down to the nearest integer

    Args:
        n (float): The number

    Returns:
        int: The input number rounded down to the nearest integer.
    """
    return int(math.floor(n))

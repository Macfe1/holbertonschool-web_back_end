#!/usr/bin/env python3
"""
This module provides a function that creates a tuple
with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple containing a string and the square of a number.

    Args:
        k (str): The key, represented as a string.
        v (Union[int, float]): The value, which is either
          an integer or a float.

    Returns:
        Tuple[str, float]: A tuple where the first element is `k`
        and the second element is `v` squared, cast to a float.
    """
    thetuple: Tuple = (k, float(v ** 2))
    return thetuple

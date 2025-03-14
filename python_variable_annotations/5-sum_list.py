#!/usr/bin/env python3
"""
This module provides a function that takes a list of floats and
sums all the numbers in it
"""


def sum_list(input_list: list[float]) -> float:
    """
    Takes a list of floats and returns their sum.

    Args:
        input_list (list[float]) : The list of floats
    Returns:
        float: The sum of the list
    """
    return float(sum(input_list))

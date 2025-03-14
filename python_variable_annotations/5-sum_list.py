#!/usr/bin/env python3
"""
This module provides a function that takes a list of floats and
sums all the numebr in it
"""


def sum_list(input_list: list[float]) -> float:
    """
    Takes a list of floats and returns their sum.

    Args:
        input_list (list[floats]) : The list of floats
    Returns:
        float: The sum of the list
    """
    return sum(input_list)

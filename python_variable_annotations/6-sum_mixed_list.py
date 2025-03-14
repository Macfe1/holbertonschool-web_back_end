#!/usr/bin/env python3
"""
This module provides a function that returns
a sum of integers and floats
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of floats and integers
    and returns their sum.

    Args:
        input_list (List[int, float]) : The list of numbers
    Returns:
        float: The sum of the list
    """
    return float(sum(mxd_lst))

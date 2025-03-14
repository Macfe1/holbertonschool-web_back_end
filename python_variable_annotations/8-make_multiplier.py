#!/usr/bin/env python3
"""
This module provides a function that generates a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given number
    by a specified multiplier.

    Args:
        multiplier (float): The number by which the
        returned function will multiply its input.

    Returns:
        Callable[[float], float]: A function that
        takes a float and returns the product
        of that float and the multiplier.
    """

    def multiplier_function(otherNumber: float) -> float:
        """
        Multiplies a given number by the stored multiplier.

        Args:
            otherNumber (float): The number to be multiplied.

        Returns:
            float: The result of multiplying otherNumber by multiplier.
        """
        return otherNumber * multiplier
    return multiplier_function

#!/usr/bin/env python3
"""
This module provides a function to compute the length of each element
in an iterable of sequences.
"""

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence elements
            (e.g., list, tuple, or other ordered iterables).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
            an element from `lst` and its corresponding length.
    """
    return [(i, len(i)) for i in lst]

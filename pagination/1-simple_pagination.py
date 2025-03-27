#!/usr/bin/env python3
"""
Pagination module for handling a dataset of popular baby names.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function calculates the start and end indexes
    for paginating a dataset.

    Args:
        page (int): The current page number (1-based index).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index
        for slicing the dataset.
    """
    start = (page - 1) * page_size
    end = start + page_size

    index_tuple = (start, end)

    return index_tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page from the dataset.

        Args:
            page (int): The page number (1-based index).
            Must be greater than 0.
            page_size (int): The number of records per page.
            Must be greater than 0.

        Returns:
            List[List[str]]: A list of rows corresponding
            to the requested page.
            Returns an empty list if the
            page is out of range.
        """

        data = self.dataset()

        assert isinstance(page, int), "page is not an integer"
        assert isinstance(page_size, int), "page_size is not an integer"

        assert page > 0, "page is not greater than zero"
        assert page_size > 0, "page_size is not greater than zero"

        index_to_paginate = index_range(page, page_size)

        if index_to_paginate[0] >= len(data):
            return []

        start = index_to_paginate[0]
        end = index_to_paginate[1]

        return list(data[start:end])

#!/usr/bin/env python3
"""
This module have a class with functions that manage
a dataset with pagination and HATEOAS
"""

from typing import Dict, List, Tuple
import math
import csv


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

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, object]:
        """
        This function takes a dataset paginated and
        returns its information as total pages, next page
        and prev page if their exists

        Args:
            page (int): The current page number (1-based index).
            page_size (int): The number of items per page.

        Returns:
            dictionarie: A dictionarie with the total pages
            the dataset paginated, the next page and prev page and
            the page
        """

        data = self.get_page(page, page_size)
        print("DATA 👁️👁️", data)
        print("LEN DATA 😁", len(data))
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = None if page + 1 > total_pages else page + 1
        prev_page = page - 1 if page != 1 else None

        dictionary = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return dictionary

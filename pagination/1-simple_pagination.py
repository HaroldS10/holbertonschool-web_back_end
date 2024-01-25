#!/usr/bin/env python3
"""
simple pagination function
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retrieves the index range from a given page and page size.
    """

    ind_start = (page - 1) * page_size
    ind_end = page * page_size

    return (ind_start, ind_end)


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
        Retrieves a page of data
        """

        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        ind_start, ind_end = index_range(page, page_size)
        data = self.dataset()
        if ind_start > len(data):
            return []
        return data[ind_start:ind_end]

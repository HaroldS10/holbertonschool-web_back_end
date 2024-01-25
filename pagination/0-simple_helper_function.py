#!/usr/bin/env python3
"""
pagination index function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ 
    Retrieves the index range from a given page and page size.
    """

    ind_start = (page - 1) * page_size
    ind_end = page * page_size

    return (ind_start, ind_end)

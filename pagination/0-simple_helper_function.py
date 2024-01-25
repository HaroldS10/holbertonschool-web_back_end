#!/usr/bin/env python3
"""
The function should return a tuple of size two,
containing a start index and an end index corresponding,
to the range of indexes to return in a list for those particular pagination parameters.
"""

from typing import Tuple

def index_range (page: int, page_size: int) -> tuple [int, int]:
    
    ind_start = (page - 1) * page_size
    ind_end = page * page_size
    
    return (ind_start, ind_end)

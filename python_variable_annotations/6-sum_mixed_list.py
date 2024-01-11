#!/usr/bin/env python3

"""
program has a single function
"""


from typing import List
from typing import Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
    function adds floats & ints of a list, returns float
    """
    return sum(input_list)

#!/usr/bin/env python3

"""
program has a single function
"""


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    gets iterable list resuts list with a tuple
    """
    return [(i, len(i)) for i in lst]

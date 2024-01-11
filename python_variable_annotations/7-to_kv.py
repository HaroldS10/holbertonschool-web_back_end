#!/usr/bin/env python3

'''
program has a single function
'''


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    function returns Tuple, first str, second float
    of square value of v
    '''
    return (k, v*v)

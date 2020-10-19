#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list
"""
from typing import List, Union
s = Union[float, int]


def sum_mixed_list(mxd_lst: List[s]) -> float:
    """
    takes a list mxd_lst of floats and
    integers and returns their sum as a float.
    """
    return sum(mxd_lst)

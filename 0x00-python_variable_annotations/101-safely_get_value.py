#!/usr/bin/env python3
"""
safely_get_value
"""
from typing import Union, Any, Mapping, List, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                    default: Union[TypeVar('T'), None] = None)\
                    -> Union[Any, TypeVar('T')]:
    """
    safely_get_value
    """
    if key in dct:
        return dct[key]
    else:
        return default

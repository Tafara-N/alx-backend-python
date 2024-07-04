#!/usr/bin/env python3

"""
Function that takes a dictionary and a key and returns the value of the key
"""

from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default

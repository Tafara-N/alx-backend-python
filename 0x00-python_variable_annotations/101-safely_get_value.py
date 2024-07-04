#!/usr/bin/env python3

"""
Function that takes a dictionary and a key and returns the value of the key
"""

from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Parameters:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): Default value to return if the key
                            is not found in the dictionary. Defaults to None.

    Return:
        The value associated with the specified key in the dictionary if the
                key is found; otherwise, the default value.
    """

    if key in dct:
        return dct[key]
    else:
        return default

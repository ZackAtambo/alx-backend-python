#!/usr/bin/env python3
"""
Type-annotated function to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return tuple of string and float
    """
    return (k, v * v)
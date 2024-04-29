#!/usr/bin/env python3
"""Document for module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function document"""
    return (k, v**2)

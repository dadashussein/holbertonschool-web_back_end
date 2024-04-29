#!/usr/bin/env python3
"""Document for module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Document for function"""
    def callable(x: float) -> float:
        return x * multiplier
    return callable

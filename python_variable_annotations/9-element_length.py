#!/usr/bin/env python3
"""Document for module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element length"""
    return [(i, len(i)) for i in lst]

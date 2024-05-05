#!/usr/bin/env python3
"""Python annotation"""
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Function document"""
    if lst:
        return lst[0]
    else:
        return None

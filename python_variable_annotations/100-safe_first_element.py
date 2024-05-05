#!/usr/bin/env python3
"""Python annotation"""
from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """document for function"""
    if lst:
        return lst[0]
    else:
        return None

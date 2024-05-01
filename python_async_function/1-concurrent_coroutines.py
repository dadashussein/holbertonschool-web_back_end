#!/usr/bin/env python3
"""Module document"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait_n document"""
    my_list = []
    for _ in range(n):
        all_delays = await wait_random(max_delay)
        my_list.append(all_delays)
    return sorted(my_list)

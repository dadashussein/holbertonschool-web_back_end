#!/usr/bin/env python3
"""Document module"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function doc"""
    my_list = []
    for _ in range(n):
        all_delays = await task_wait_random(max_delay)
        my_list.append(all_delays)
    return sorted(my_list)

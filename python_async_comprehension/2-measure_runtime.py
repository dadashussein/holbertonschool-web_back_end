#!/usr/bin/env python3
"""Python async generator task"""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Async_comprehension 4 times in parallel"""
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.time() - start_time

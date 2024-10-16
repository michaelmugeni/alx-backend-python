#!/usr/bin/env python3
import asyncio
import time
from typing import List
from async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel using asyncio.gather.

    Returns:
        Total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time

measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)


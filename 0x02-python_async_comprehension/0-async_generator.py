#!/usr/bin/env python3

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.

    Returns:
        An asynchronous generator yielding random floats between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())


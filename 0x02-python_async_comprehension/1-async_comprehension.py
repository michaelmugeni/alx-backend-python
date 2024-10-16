#!/usr/bin/env python3
import asyncio
from typing import List, AsyncGenerator
from async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator.

    Returns:
        List of 10 random float numbers.
    """
    return [number async for number in async_generator()]

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())


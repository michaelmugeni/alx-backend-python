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

async def main():
    result = await async_comprehension()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())



#!/usr/bin/env python3
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
@@ -12,12 +11,5 @@ async def wait_n(n: int, max_delay: int) -> List[float]:
    queue, array = [], []
    for _ in range(n):
        queue.append(wait_random(max_delay))
    for q in asyncio.as_completed(queue):
        result = await q
        array.append(result)
    return array
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))


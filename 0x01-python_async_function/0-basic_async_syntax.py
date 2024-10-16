#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int =10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random( ))) # 9.034261504534394
print(asyncio.run(wait_random(5)))  # 1.6216525464615306
print(asyncio.run(wait_random(15))) # 10.634589756751769



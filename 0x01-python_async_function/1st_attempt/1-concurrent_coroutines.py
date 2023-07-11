#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async
"""


import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    delay = []
    for _ in range(n):
        delay.append(asyncio.create_task(wait_random(max_delay)))
    return [await delay for delay in asyncio.as_completed(delay)]

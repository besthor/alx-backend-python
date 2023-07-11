#!/usr/bin/env python3
"""4. Tasks"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of delays in ascending order"""
    delays = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]

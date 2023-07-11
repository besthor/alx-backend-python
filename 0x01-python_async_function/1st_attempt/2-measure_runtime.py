#!/usr/bin/env python3
"""Measure the runtime"""


import asyncio
import random
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns total_time / n"""
    t1 = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    t2 = time.perf_counter()
    return (t2 - t1) / n

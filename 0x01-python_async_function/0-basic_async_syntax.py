#!/usr/bin/env python3
''' Description: asynchronous coroutine that takes in an integer argument
                 (max_delay, with a default value of 10) named wait_random
                 that waits for a random delay between 0 and max_delay
                 (included and float value) seconds and eventually returns it
    Arguments: max_delay: int = 10
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait up to max_delay seconds and then return length of delay. '''
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay

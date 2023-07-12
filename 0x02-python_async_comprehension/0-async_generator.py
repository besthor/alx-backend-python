#!/usr/bin/env python3
''' Task: A coroutine called async_generator that takes no
                 arguments.
                 The coroutine will loop 10 times, each time asynchronously
                 wait 1 second, then yield a random number between 0 and 10.
                 Use the random module.
'''

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Generator that yields a random value between 0 and 10 every second,
        10 times. '''
    for i in range(10):
        await sleep(1)
        yield 10 * random()

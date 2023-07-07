#!/usr/bin/env python3
''' Description: Accepts a float multiplier as argument and returns a function
                 that multiplies a float by multiplier
    Parameters: multiplier: float
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Outputs function that multiplies float by `multiplier`. '''
    return lambda x: x * multiplier

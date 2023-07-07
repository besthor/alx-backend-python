#!/usr/bin/env python3
''' Description:takes a float n as argument and returns the floor of the float
    Parameter: n: float
'''


def floor(n: float) -> int:
    ''' Return largest int value less than or equal to n. '''
    return int(n) if n >= 0 else int(n) - 1

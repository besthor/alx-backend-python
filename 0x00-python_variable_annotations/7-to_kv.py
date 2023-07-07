#!/usr/bin/env python3
''' Description: takes a string k and an int OR float v as arguments and
                 returns a tuple. The first element of the tuple is the
                 string k.
                 The second element is the square of the int/float v and
                 should be annotated as a float.
    Arguments: k: str, v: Union[int, float]
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Return tuple consisting of k and the square of v. '''
    return (k, v * v)

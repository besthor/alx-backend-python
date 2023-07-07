#!/usr/bin/env python3
''' Description: accepts a list mxd_lst of floats and integers and
    returns their sum as a float.
    Parameters: mxd_lst: List[Union[int, float]]
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Outputs sum of elements of mxd_list. '''
    return sum(mxd_lst)

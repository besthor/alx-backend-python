#!/usr/bin/env python3
''' Description: Use mypy to validate the following piece of code
                 and apply any necessary changes.
    Parameters: lst: Tuple, factor: int = 2
'''

from typing import Union, Any, Mapping, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    ''' Variable Annotation for list '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))

#!/usr/bin/env python3
""" asynchronous coroutine """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    '''
    Returns list of  delays.
    '''
    result = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(result)

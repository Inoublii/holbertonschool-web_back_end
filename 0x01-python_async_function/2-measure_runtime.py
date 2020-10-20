#!/usr/bin/env python3
'''
Contains a coroutine.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Returns the execution time for wait_n(n, max_delay) devided by n.
    '''
    strt = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - strt) / n)

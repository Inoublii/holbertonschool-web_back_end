#!/usr/bin/env python3
"""
Logging module.

"""
import re
from typing import List


def filter_datum(fields: List[str],
				 redaction: str,
				 message: str,
                 separator: str) -> str:
    """ Logging module. """
    lst = message.split(separator)

    for f in fields:
        for i in range(len(lst)):
            if lst[i].startswith(f):
                subst = f + '=' + redaction
                lst[i] = re.sub(lst[i], subst, lst[i])

    return separator.join(lst)

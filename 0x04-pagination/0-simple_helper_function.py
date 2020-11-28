#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
"""
def index_range(page, page_size):
	"""
	function named index_range that takes two integer arguments:
    page and page_size.
	"""
	x = (page - 1) * page_size
	return (x, x + page_size)

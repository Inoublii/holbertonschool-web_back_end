#!/usr/bin/env python3

"""
function named index_range that takes two integer arguments
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                read = csv.reader(f)
                data = [row for row in read]
            self.__dataset = data[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Use assert to verify"""
        assert (isinstance(page, int) and isinstance(
            page_size, int)and page > 0 and page_size > 0)
        range = index_range(page, page_size)
        self.dataset()
        return self.__dataset[range[0]:range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A method that takes the same arguments (and defaults) as get_page"""
        data = self.get_page(page, page_size)
        total = math.ceil(len(self.__dataset) / page_size)
        next = page + 1 if page < total else None
        prev = page - 1 if page > 1 else None
        return {'page_size': len(data), 'page': page, 'data': data,
                'next_page': next, 'prev_page': prev, 'total_pages': total}

    def index_range(self, page, page_size):
        """
        function named index_range that takes two integer arguments
        """
        x = (page - 1) * page_size
        return (x, x + page_size)

#!/usr/bin/env python3

"""
function named inex_range
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def index_range(self, page, page_size):
        """function named index_range that takes two integer arguments:"""
        x = (page - 1) * page_size
        return (x, x + page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """verify that both arguments are integers greater than 0"""
        assert (isinstance(page, int) and isinstance(
            page_size, int) and page > 0 and page_size > 0)
        range = Server().index_range(page, page_size)
        self.dataset()
        return self.__dataset[range[0]:range[1]]

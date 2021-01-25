#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def indexed_dataset(self):
            """Dataset indexed by sorting position"""
            if self.__indexed_dataset is None:

                dataset = self.dataset()

                truncated_dataset = dataset[:1000]

                self.__indexed_dataset = {

                    i: dataset[i] for i in range(len(dataset))
                }
            return self.__indexed_dataset

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                read = csv.reader(f)
                data = [row for row in read]
            self.__dataset = data[1:]
        return self.__dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) :
            pass

    def get_hyper_index(self, index: int = None, page_size: int = 10):
        """The method should return a dictionary"""
        assert (isinstance(
            index, int)and index in range(len(self.__indexed_dataset)))
        data = []
        diff = 0
        row = index
        while diff < page_size and row < len(self.__indexed_dataset):
            if row in self.__indexed_dataset:
                data.append(self.__indexed_dataset[row])
                row += 1
                diff += 1

            else:
                row += 1
        if row < len(self.__indexed_dataset):
            next = row
        else:
            next = None
        return {'index': index, 'next_index': next,
                'page_size': len(data), 'data': data}

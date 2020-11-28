#!/usr/bin/python3
"""FIFO cashing"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO CLASS """
    def __init__(self):
        """ self init """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        assign to the dictionary"""
        if key and item:
            self.order.append(key)
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.order[0]]
                    print("DISCARD:", self.order[0])
                    self.order.pop(0)
                self.cache_data[key] = item

    def get(self, key):
        """
        return the value of key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None

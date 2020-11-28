#!/usr/bin/python3
""" FIFO Cache """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache Class """
    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value of key in self.cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None

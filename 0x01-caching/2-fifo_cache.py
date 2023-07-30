#!/usr/bin/env python3
""" BaseCaching moduel
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Define a FIFO Caching system
    """

    def __init__(self_):
        """
        Initialize the class with parent's system
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Cache a key-value
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

        def get(self, key):
            """
            Return the linked value to a given key, or None
            """
            if key is not Nono and key in self.cache_data.keys():
                return self.cahce_data[key]
            return None

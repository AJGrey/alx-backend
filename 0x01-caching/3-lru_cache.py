#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """
    LRUCache defines a caching system using the LRU algorithm
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.lru_queue = OrderedDict()

    def put(self, key, item):
        """
        Cache a key-value pair using LRU algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                oldest_key = next(iter(self.lru_queue))
                del self.cache_data[oldest_key]
                del self.lru_queue[oldest_key]
                print("DISCARD: {}".format(oldest_key))

        if key in self.lru_queue:
            # Move the key to the end to mark it as the most recently used
            self.lru_queue.move_to_end(key)
        else:
            self.lru_queue[key] = True

        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key using LRU algorithm, or None
        """
        if key is not None and key in self.cache_data:
            # Move the key to the end to mark it as the most recently used
            self.lru_queue.move_to_end(key)
            return self.cache_data[key]
        return None


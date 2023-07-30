#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache defines a caching system using the MRU algorithm
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.mru_queue = OrderedDict()

    def put(self, key, item):
        """
        Cache a key-value pair using MRU algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                most_recent_key = next(reversed(self.mru_queue))
                del self.cache_data[most_recent_key]
                del self.mru_queue[most_recent_key]
                print("DISCARD: {}".format(most_recent_key))

        self.mru_queue[key] = True
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key using MRU algorithm, or None
        """
        if key is not None and key in self.cache_data:
            self.mru_queue.move_to_end(key)
            return self.cache_data[key]
        return None

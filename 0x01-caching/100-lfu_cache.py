#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache defines a caching system using the LFU algorithm
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.lru_queue = OrderedDict()

    def put(self, key, item):
        """
        Cache a key-value pair using LFU algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            least_frequent_keys = [
                k for k, freq in self.frequency.items() if freq == min_freq
                ]

            if len(least_frequent_keys) > 1:
                lru_key = next(iter(self.lru_queue))
                least_frequent_keys.remove(lru_key)

            least_frequent_key = least_frequent_keys[0]
            del self.cache_data[least_frequent_key]
            del self.frequency[least_frequent_key]
            del self.lru_queue[least_frequent_key]
            print("DISCARD: {}".format(least_frequent_key))

        self.frequency[key] += 1
        self.lru_queue[key] = True
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key using LFU algorithm, or None
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.lru_queue.move_to_end(key)
            return self.cache_data[key]
        return None

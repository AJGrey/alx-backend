#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class that inherits from BaseCaching
    Methods:
        put(key, item) - store a key-value
        get(key) - return the value associated with a key
    """

    def put(self, key, item):
        """
        Store a key-value
        Args:
            Key
            Item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value linked to key.
        If key is None or doesn't exist, return None
        """
        return self.cache_data.get(key, None)

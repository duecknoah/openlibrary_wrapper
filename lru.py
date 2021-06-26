"""
Least Recently Used (LRU) cache allows us to
keep what we use often up to the Nth least used
"""
class LRUCache(object):

    def __init__(self, capacity):
        """Stores the cache in a dictionary, where the key and value are stored.
        The order of recently used is stored in the order list
        :type capacity: int
        """
        self.cap = capacity
        self.order = []
        self.cache = {}
    def get(self, key):
        """Gets an item from the cache
        :rtype: int
        """
        # If in the cache, put at the front as it is
        # the most recently used
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return -1 # nothing found, return -1


    def set(self, key, value):
        """Sets/adds an item to the cache, popping least recently used item
        from the cache if we are at capacity
        :type key: int
        :type value: int
        :rtype: nothing
        """

        # Remove old position from cache if already existed
        # else we want to
        if key in self.cache:
            self.order.remove(key)
        elif len(self.order) == self.cap:
                self.cache.pop(self.order[0])
                self.order.pop(0)

        self.order.append(key)
        self.cache[key] = value

    def __str__(self):
        return str(self.cache)

    def __len__(self):
        return len(self.order)

    def getOrder(self):
        return self.order
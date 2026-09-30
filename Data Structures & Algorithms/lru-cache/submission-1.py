from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.usage = deque()
        

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val != -1:
            self.usage.remove(key)
            self.usage.append(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.usage:
            self.usage.remove(key)
        self.cache[key] = value
        self.usage.append(key)

        if len(self.cache) > self.capacity:
            to_remove = self.usage.popleft()
            del self.cache[to_remove]
        

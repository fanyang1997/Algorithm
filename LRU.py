# leetcode 146
# LRU cache

class double_linked_list:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = double_linked_list(None, None)
        self.tail = double_linked_list(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    
    def put(self, key, value):
        if key not in self.cache:
            node = double_linked_list(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if len(self.cache) > self.capacity:
                self.remove_tail()
                self.cache.pop(self.tail.prev.key)
        else:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_to_head(node)


    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_to_head(node)
            return node.value
        else:
            return -1

    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
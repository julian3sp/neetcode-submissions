class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #map key to nodes
        self.capacity = capacity

        # left = LRU, right=most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    # remove from list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev


    # insert at right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from linked list and delete LRU Node from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



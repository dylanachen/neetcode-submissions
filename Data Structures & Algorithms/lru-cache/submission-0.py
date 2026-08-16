class Node:
    def __init__(self, key, val):
        # use a doubly linked list to access both ends and re-order upon calling a key
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # using a hashmap key:node
        self.cap = capacity
        self.cache = {}

        # left and right pointers to the ends of the DLL
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # remove left
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # insert at right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # reordering to most recent upon call
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # replacing if the key already exists
        if key in self.cache:
            self.remove(self.cache[key])
        # always adding a new key to the cache and the DLL
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from DLL and delete LRU from the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
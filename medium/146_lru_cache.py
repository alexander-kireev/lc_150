class ListNode:
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.list_map = {}
        self.capacity = capacity
        self.length = 0
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        
        
    def get(self, key: int) -> int:
        if key in self.list_map:
            value = self.list_map[key].value
            self.remove_node(key)
            self.add(key, value)
            return value
        else:
            return -1
        
    
    def put(self, key: int, value: int) -> None:
        if self.list_map.get(key):
            self.remove_node(key)
        elif self.length == self.capacity:
            self.remove_lru()
        self.add(key, value)

    def add(self, key: int, value: int) -> None:
        # make new node
        new_node = ListNode(key, value)

        # insert new node between dummy head and old head
        new_node.prev = self.dummy_head
        new_node.next = self.dummy_head.next
        self.dummy_head.next.prev = new_node
        self.dummy_head.next = new_node

        # add new node to map
        self.list_map[key] = new_node

        self.length += 1

    def remove_node(self, key: int):
        # get prev and next nodes
        prev_node = self.list_map[key].prev
        next_node = self.list_map[key].next

        # connect prev and next nodes
        prev_node.next = next_node
        next_node.prev = prev_node

        # completely disconnect and remove node
        node = self.list_map[key]
        node.next = None
        node.prev = None
        self.list_map.pop(key)

        self.length -= 1

    def remove_lru(self):
        # get last and before last nodes
        last = self.dummy_tail.prev
        before_last = last.prev

        # make before last the new last node
        before_last.next = self.dummy_tail
        self.dummy_tail.prev = before_last

        # completely disconnect removed node
        last.next = None
        last.prev = None
        self.list_map.pop(last.key)

        self.length -= 1



def show(cache, label):
    print(label)
    print("map keys:", list(cache.list_map.keys()))
    print("length:", cache.length)

    cur = cache.dummy_head.next
    values = []
    while cur is not cache.dummy_tail:
        values.append(cur.value)
        cur = cur.next

    print("list values MRU -> LRU:", values)
    print("-" * 50)



cache = LRUCache(2)

cache.put(1, 1)
show(cache, "put(1, 1)")

cache.put(2, 2)
show(cache, "put(2, 2)")

print(cache.get(1))  # 1
show(cache, "get(1)")

cache.put(3, 3)
show(cache, "put(3, 3)")

print(cache.get(2))  # -1

cache.put(4, 4)
show(cache, "put(4, 4)")

print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4




cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)
show(cache, "after put 1, put 2")

cache.put(1, 100)
show(cache, "after updating key 1 to 100")

print(cache.get(1))  # 100
print(cache.get(2))  # 20



cache = LRUCache(1)

cache.put(1, 1)
show(cache, "put(1, 1)")

print(cache.get(1))  # 1

cache.put(2, 2)
show(cache, "put(2, 2)")

print(cache.get(1))  # -1
print(cache.get(2))  # 2




cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))  # 1

cache.put(3, 3)

print(cache.get(1))  # 1
print(cache.get(2))  # -1
print(cache.get(3))  # 3

show(cache, "final state")
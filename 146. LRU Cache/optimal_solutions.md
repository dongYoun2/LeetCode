[Problem](https://leetcode.com/problems/lru-cache/)

The three solutions below all perform with the equivalent complexity:
- TC: `get()` and `put()` operations in $O(1)$
- SC: structural space (LRU Cache) - $O(capacity)$, auxiliary space per operation (get/put) - $O(1)$
<br>

## Doubly Linked List with Hashmap (From Scratch)

- [Submission](https://leetcode.com/problems/lru-cache/submissions/1614175674)

```python
class DListNode: # doubly linked list's node
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> DListNode

        self.head = DListNode(-1, -1)    # head's dummy node
        self.tail = DListNode(-1, -1)    # tail's dummy node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node):
        next_node = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = next_node
        next_node.prev = node

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del_node = self.cache[key]
            self._remove(del_node)
        elif len(self.cache) == self.cap:
            lru_node = self.tail.prev    # least recently used node
            del self.cache[lru_node.key]    # same as `self.cache.pop(lru_node.key)`
            self._remove(lru_node)

        # updating or inserting to a most recently used position
        new_node = DListNode(key, value)
        self._add_to_front(new_node)
        self.cache[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

```
<br>

## Using Python dictionary

Python 3 dictionary stores key-value pairs in order. To perform `put()` in $O(1)$ time, we can use `next(iter())`, which emulates the behavior of `OrderedDict`'s `popitem(last=False)` ([reference](https://docs.python.org/3/library/collections.html#collections.OrderedDict:~:text=The%20popitem(),if%20it%20exists.)).

- [Submission](https://leetcode.com/problems/lru-cache/submissions/1614180369/)

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        v = self.cache.pop(key) # for rank update
        self.cache[key] = v

        return v

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key] # same as `self.cache.pop(key)`
        elif len(self.cache) == self.cap:
            lru_key = next(iter(self.cache.keys())) # TC: O(1)
            del self.cache[lru_key] # same as `self.cache.pop(lru_key)`

        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

```
<br>

## Using Python `OrderedDict`

- [Submission](https://leetcode.com/problems/lru-cache/submissions/1614182763/)

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        self.cache.move_to_end(key) # for rank update
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key] # same as `self.cache.pop(key)`
        elif len(self.cache) == self.cap:
            self.cache.popitem(last=False) # works as FIFO (LIFO if `last` is `True`)

        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

```
<br>

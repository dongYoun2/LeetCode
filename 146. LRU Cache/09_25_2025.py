# submission: https://leetcode.com/problems/lru-cache/submissions/1782636333/
# runtime: 119 ms (beats 64.59%), memory: 78.06 MB (beats 27.06%)
# 50 min

# TC: O(1), for get and put
# SC: O(n), `key_to_node` and keeping doubly linked list


# for Speechify interview prep. i knew i had to use doubly linked list with hashmap, but still took quite longer than expected.


class Node:
    def __init__(self, key: int=-1, val: int=-1, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.max_cap = capacity
        self.curr_cap = 0

        self.head = Node()    # head dummy node
        self.tail = Node(prev=self.head) # tail dummy node
        self.head.nxt = self.tail


    def unlink(self, node):
        prev, nxt = node.prev, node.nxt

        prev.nxt = nxt
        nxt.prev = prev


    def insert_end(self, node):
        prev = self.tail.prev

        prev.nxt = node
        node.prev = prev

        node.nxt = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        # update most recently used key and node
        find_node = self.key_to_node[key]
        self.unlink(find_node)
        self.insert_end(find_node)

        return find_node.val


    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1: # get() move nodes to the tail
            self.key_to_node[key].val = value
            return

        new_node = Node(key, value)
        self.insert_end(new_node)
        self.key_to_node[key] = new_node

        if self.curr_cap >= self.max_cap:   # cache was full (remove LRU node)
            del_node = self.head.nxt
            del_key = del_node.key
            self.unlink(del_node)

            del self.key_to_node[del_key]
        else:
            self.curr_cap += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# notes while solving:
# h (lru)                 t
# dummy <-> 1 <-> 2 <-> dummy
# 2 <-> 1

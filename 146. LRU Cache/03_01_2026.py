# submission: https://leetcode.com/problems/lru-cache/submissions/1935043856/
# runtime: 119 ms (beats 64.59%), memory: 78.79 MB (beats 21.37%)
# 31 min

# time and space complexities are the same as the README. refer to it for details.


# i knew that LRU cache can be implemented with doubly linked list, so i directly attempted with it. but took a little longer than expected.

# cf.) there are some duplicates in the code, and some code can be modularized in functions better. refer to the README for details.


class DLNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.capacity = capacity
        self.head = self.tail = DLNode(-1, -1)  # dummy node
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def move_front(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        tmp = self.head.next

        node.next = tmp
        tmp.prev = node

        self.head.next = node
        node.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.key_to_node: return -1

        curr = self.key_to_node[key]
        self.move_front(curr)

        return curr.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            curr = self.key_to_node[key]
            curr.value = value
            self.move_front(curr)
        else:
            new_node = DLNode(key, value, self.head, self.head.next)
            self.head.next = new_node
            new_node.next.prev = new_node

            self.key_to_node[key] = new_node


        if len(self.key_to_node) > self.capacity:
            del_key = self.tail.prev.key
            del_node = self.tail.prev

            del_node.prev.next = self.tail
            self.tail.prev = del_node.prev

            del self.key_to_node[del_key]
            del del_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# submission: https://leetcode.com/problems/lru-cache/submissions/1613612409/
# time limit exceeded (TLE)
# 57 min

# TC: get - O(n), put - O(n), where n is the number of nodes in the linked list
# SC: LRU Cache - O(capacity), auxiliary space per operation (get/put) - O(1)

# From LeetCode Top Interview 150 - Linekd List

# The below code's submission fails on the 22nd test case out of 23, showing time limit exceeded (TLE). In the question requires to implement `get` and `put` methods in O(1) time complexity, but I didn't read the question carefully (I found this out later, and reminded me to always read the question carefully), so I solved it in a brute force way with single linked list that stores the nodes in the order of their usage... But the logic itself is correct, so it works fine when the number of nodes is relatively small.

# Plus, debugging took quite a while for the below naive approach. Several struggles are as follows:
# 1. In the case of a key not existing in the `put` method, the capacity check logic (whether the linked list is full) needs to come after the new node insertion logic, not before. Otherwise, it fails when the capacity equals 1. When the `put` is called three times, at the second call, the `dummy_head` and `tail` are disconnected, leading `dummy_head.next` being `None` on the third call; thus, "AttributeError: 'NoneType' object has no attribute 'next'" error rises.
# 2. Missing `self.tail.next = None` in the `get` method caused the linked list to be circular.
# 3. Forgot to consider that a node with the existing key has to be updated with the new value. (code related to `found_val = self.get(key)` in the `put` method)


# A solution with `get` and `put` in O(1) time can be found in the markdown file.


class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        assert capacity >= 1

        self.MAX_CAP = capacity
        self.curr_cap = 0

        self.dummy_head = Node(-1, -1)
        self.tail = self.dummy_head


    def get(self, key: int) -> int:
        curr = self.dummy_head
        while curr.next and curr.next.key != key:
            curr = curr.next

        if curr.next is None:   # key not found
            return -1

        # update found node (curr) to the most recent place (at the end of the list)
        self.tail.next = curr.next
        self.tail = self.tail.next

        curr.next = curr.next.next
        self.tail.next = None

        return self.tail.val


    def put(self, key: int, value: int) -> None:
        found_val = self.get(key)
        if found_val != -1: # update value since key exists
            self.tail.val = value   # after calling get, the tail is the node with the key (position updated)
            return

        # first add the node at the end
        self.tail.next = Node(key, value)
        self.tail = self.tail.next
        self.curr_cap += 1

        if self.curr_cap > self.MAX_CAP:   # remove the LRU node if capacity exceeded
            self.dummy_head.next = self.dummy_head.next.next
            self.curr_cap -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

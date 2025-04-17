## Using Hashmap to Detect Cycle in a Linked List

[Problem](https://leetcode.com/problems/linked-list-cycle/)

- TC: $O(n)$, where n is the number of nodes in the linked list
- SC: $O(n)$ (Python `set`)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        s = set()
        while curr:
            node_id = id(curr)
            if node_id in s:
                return True

            s.add(node_id)
            curr = curr.next

        return False
```
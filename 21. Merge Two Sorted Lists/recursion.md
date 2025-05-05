[Problem Link](https://leetcode.com/problems/merge-two-sorted-lists/description/)

## Recursive Approach

- [submission](https://leetcode.com/problems/merge-two-sorted-lists/submissions/1626236787/)
- TC: $O(n + m)$, where n and m are the lengths of the two lists.
- SC: $O(n + m)$ (recursion stack space)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2

        if list2 == None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

```
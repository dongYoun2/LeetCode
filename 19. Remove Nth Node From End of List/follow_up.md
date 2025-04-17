## One Pass Solution

[Problem](https://leetcode.com/problems/linked-list-cycle/)

The below uses a two-pointer approach to solve the follow-up question. Although `04_17_2025_follow_up.py` solves the problem in one pass, it requires an extra $O(n)$ space, which is still suboptimal. By always keeping the `trailing` pointer behind `n` nodes of the `ahead` pointer while traversing, we can easily find the node to remove without any need for additional memory.

Just like the [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), I realized it's always good to keep in mind that the **two-pointer algorithm** can be beneficial for solving linked list-related problems with only a constant space.
<br>

- [Submission](https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1609523240/)
- TC: $O(n)$, where n is the number of nodes in the linked list
- SC: $O(1)$

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        ahead = trailing = dummy

        for _ in range(n + 1):
            ahead = ahead.next

        # Move both until ahead hits the end
        while ahead:
            ahead = ahead.next
            trailing = trailing.next

        # Now trailing.next is the node to remove
        trailing.next = trailing.next.next

        return dummy.next
```
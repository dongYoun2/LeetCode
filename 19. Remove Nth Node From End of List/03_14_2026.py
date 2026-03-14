# submission: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1947893911/
# runtime: 0 ms (beats 100.00%), memory: 19.32 MB (beats 57.70%)
# 12 min
# this solution directly solves the follow-up question using a two-pointer approach.

# complexity analysis is the same as the markdown file. refer to it for more details.


# pretty straightforward solution.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        assert head is not None

        dummy = ListNode(-1, head)
        curr = ahead = dummy
        for _ in range(n):
            ahead = ahead.next

        assert ahead is not None
        while ahead.next is not None:
            ahead = ahead.next
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next

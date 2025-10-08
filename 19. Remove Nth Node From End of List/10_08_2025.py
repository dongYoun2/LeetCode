# submission: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1795330156/
# runtime: 0 ms, memory: 17.9 MB
# this solution solves the follow-up question with a constant space

# 7 min
# TC: O(n), where n is the number of nodes in the linked list
# SC: O(1)


# we can solve this problem in one pass with a constant space by usig slow and fast pointers approach.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        assert head is not None

        dummy = ListNode(-1, head)
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        prev = slow # # slow becomes a node before the one to remove
        prev.next = prev.next.next

        return dummy.next

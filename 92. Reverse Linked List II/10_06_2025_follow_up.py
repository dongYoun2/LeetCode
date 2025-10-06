# submission: https://leetcode.com/problems/reverse-linked-list-ii/submissions/1793431207/
# runtime: 0 ms, memory: 17.74 MB
# this solution solves the follow-up question.

# 26 min (includes time writing 10_06_2025.py)
# TC: O(n), where n is the number of nodes in the linked list (one-pass alg.)
# SC: O(1)


# after solving 10_06_2025.py, i moved on to the follow-up quesiton. solving in one pass was pretty straightforward by refactoring the code from 10_06_2025.py. just slight modifications are needed.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        assert head

        def reverse_list(node, cnt):
            assert node
            mark_end = node
            prev = nxt = None
            curr = node

            while curr and cnt > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                cnt -= 1

            if curr:    # leftover exists
                mark_end.next = curr

            return prev


        dummy_node = ListNode(-501, head)
        start = dummy_node
        for _ in range(left - 1):
            start = start.next

        temp1 = start   # mark position to concat at the front after reversing
        start = start.next

        reversed_start = reverse_list(start, right - left + 1)
        temp1.next = reversed_start

        return dummy_node.next

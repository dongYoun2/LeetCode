# problem: https://leetcode.com/problems/partition-list/
# submission: https://leetcode.com/problems/partition-list/submissions/1612621671/

# 32 min
# TC: O(n), where n is the number of nodes in the linked list
# SC: O(1)

# From LeetCode Top Interview 150 - Linekd List

# I think the key point for this problem is to use two left and right pointers to keep appending the nodes for the left partition and the right partition, respectively. At first, I tried to find the first node for the left and right partition, then initialize the left and right pointers with them. Then, I tried to scan the main linked list once, but it got somewhat complicated. After realizing I can simply use two dummy nodes for left and right pointers, the main loop scanned through the linked list (with `curr`) and appended the nodes to the left and right partitions, comparing the value with `x`.

# After coding it up, I had an error due to missing `r_curr.next = None` after the while loop. This is necessary to terminate the right partition, which breaks the cycle and makes the linked list valid. Debugging this took a while, but I finally got it working.

# cf.) The early return for `head is None` is not necessary, since the rest of the logic is also valid for the empty linked list (i.e., `head` is None) case.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None: return None

        left_dummy = ListNode(-201)
        right_dummy = ListNode(-201)

        l_curr = left_dummy
        r_curr = right_dummy

        curr = head
        while curr:
            if curr.val < x:
                l_curr.next = curr
                l_curr = l_curr.next
            else:
                r_curr.next = curr
                r_curr = r_curr.next

            curr = curr.next

        r_curr.next = None
        l_curr.next = right_dummy.next

        return left_dummy.next

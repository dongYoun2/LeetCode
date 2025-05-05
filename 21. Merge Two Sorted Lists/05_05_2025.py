# problem: https://leetcode.com/problems/merge-two-sorted-lists/
# submission: https://leetcode.com/problems/merge-two-sorted-lists/submissions/1626230671/

# 5 min
# TC: O(n + m), wher e n and m are the lengths of the two lists
# SC: O(1) (space for answer list is not counted)

# From LeetCode Top Interview 150 - Linked List

# This is a second time solving this question. I have solved it on 10/27/2024.

# The problem can also be solved using recursion. For more details, refer to the markdown file.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode(-101)

        ptr1, ptr2 = list1, list2
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val < ptr2.val:
                curr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                curr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next

            curr = curr.next

        curr.next = ptr1 if ptr1 is not None else ptr2  # append remaining nodes

        return dummy.next

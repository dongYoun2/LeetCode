# submission: https://leetcode.com/problems/sort-list/submissions/1648431841/

# 33 min
# runtime: 214 ms, memory: 32.91 MB
# TC: O(n log n), where n is the number of nodes in the linked list.
# SC: O(log n) (for the recursive stack sapce)


# From LeetCode Top Interview 150 - Divide & Conquer

# This is a classic divide-and-conquer problem. The solution below is simply a merge sort on a linked list. In merge sort, there are two main steps:
# 1. **Divide**: Split the linked list into two halves.
# 2. **Conquer**: Recursively sort each half and then merge the two sorted halves.

# In the code, below each function's role is as follows:
# - `merge_sorted_list(head1, head2)`: Merges two sorted lists into one (in Conquer step)
# - `merge_sort(head)`: Recursively splits and sorts the list (in both Divide and Conquer steps)

# cf.) The Answer to the follow-up question would be to perform the merge sort iteratively. Moreover, splitting the list into halves can also be done by using the fast and slow pointers, resulting in a one-pass splitting. Refer to the markdown file for more details.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_sorted_list(head1, head2):
            ptr = dummy = ListNode()

            curr1 = head1
            curr2 = head2

            while curr1 is not None and curr2 is not None:
                if curr1.val < curr2.val:
                    ptr.next = curr1
                    curr1 = curr1.next
                else:
                    ptr.next = curr2
                    curr2 = curr2.next

                ptr = ptr.next

            remaining = curr1 or curr2
            while remaining is not None:
                ptr.next = remaining

                remaining = remaining.next
                ptr = ptr.next

            return dummy.next


        def merge_sort(head):
            if head is None:    # empty list
                return None

            if head.next is None:   # single node
                return head

            # Count the number of nodes in the linked list and split it into halves.
            n = 0
            curr = head
            while curr is not None:
                curr = curr.next
                n += 1

            prev = None
            head2 = head
            for _ in range(n // 2):
                prev = head2
                head2 = head2.next

            if prev is not None:
                prev.next = None

            sorted_head = merge_sort(head)  # sort the first half
            sorted_head2 = merge_sort(head2)    # sort the second half

            sorted_list = merge_sorted_list(sorted_head, sorted_head2)

            return sorted_list


        return merge_sort(head)
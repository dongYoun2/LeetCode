# problem: https://leetcode.com/problems/linked-list-cycle/
# submission: https://leetcode.com/problems/linked-list-cycle/submissions/1609476952/

# 8 min
# TC: O(n), where n is the number of nodes in the linked list
# SC: O(1)

# From LeetCode Top Interview 150 - Linekd List

# This is the second time solving this problem. I first solved it on 11/02/2024. At that time, I solved it using a hash table to keep track of the nodes I had traversed, which needed O(n) space. I remembered the O(1) space approach using slow and fast pointers, as it was an interesting idea. This algorithm is also known as Floyd's Cycle Finding Algorithm." Therefore, this time, I coded it up directly with this approach. The code using a hash table can be found in the markdown file.

# The code below also meets the condition for the Follow-up question, which requires the use of only constant memory.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and slow:
            fast = fast.next
            if not fast: return False

            fast = fast.next
            slow = slow.next

            if fast == slow:
                return True

        return False

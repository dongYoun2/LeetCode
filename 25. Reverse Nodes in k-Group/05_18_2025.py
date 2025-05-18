# problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
# submission: https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/1637528792/

# 57 min
# runtime: 0 ms, memory: 18.7 MB
# TC: O(n), where n is the number of nodes in the linked list
# SC: O(1)

# From LeetCode Top Interview 150 - Linked List

# I came up with the idea quite quickly, but the implementation and debugging took a bit of time. Personally, adding the remaining nodes to the end was a bit confusing. I think it's because I was trying to implement it within the loop. Due to this separate logic, the main loop gets harder to follow, and the code becomes messy. Refactored code can be found in the markdown file.

# since this is an iteartive approach, it meets the follow-up question, which requires to solve in O(1) space complexity. This problem can also be solved using recursion. For more details, also refer to the markdown file.

# cf.) Here `r_head, r_tail = reverse_linked_list(curr)`, `r_tail` is actually the same as `curr` since `curr` is the head of the list to be reversed.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        assert head is not None

        def reverse_linked_list(ptr):
            assert ptr is not None

            prev = nxt = None
            curr = ptr

            while curr:
                nxt = curr.next
                curr.next = prev

                prev = curr
                curr = nxt

            return prev, ptr   # (head, tail) for the reversed list


        def find_kth_node(ptr):
            if ptr is None: return None

            find = ptr
            for _ in range(k-1):
                find = find.next
                if find is None: break

            return find


        new_head = None
        curr = head
        prev_r_tail = None

        while True:
            kth = find_kth_node(curr)   # first kth is always not None since k <= n

            if kth is None: # remain left-out nodes as it is
                prev_r_tail.next = curr
                break

            next_start = kth.next
            kth.next = None

            r_head, r_tail = reverse_linked_list(curr)

            if prev_r_tail is not None: prev_r_tail.next = r_head

            if new_head is None: new_head = r_head

            prev_r_tail = r_tail
            curr = next_start

        return new_head

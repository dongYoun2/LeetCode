# submission: https://leetcode.com/problems/reverse-linked-list-ii/submissions/1793424174/
# runtime: 0 ms, memory: 18.05 MB

# 20 min
# TC: O(n), where n is the number of nodes in the linked list
# SC: O(1)

# pretty straightforward approach. once you separate out the logic for reversing the linked list, the remaining part is to simply mark the positions to concatenate the head and tail of the reversed list segment.

# one trick is to prepend a dummy node to make sure the node to concatenate at the front of the reversed list always exists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        assert head

        def reverse_list(node):
            assert node
            mark_end = node
            prev = nxt = None
            curr = node

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev, mark_end   # reversed_start, reversed_end


        dummy_node = ListNode(-501, head)
        start = dummy_node
        for _ in range(left - 1):
            start = start.next

        temp1 = start   # mark position to concat at the front after reversing
        start = start.next
        end = start
        for _ in range(right - left):
            end = end.next

        temp2 = end.next    # mark position to concat at the end after reversing
        end.next = None

        reversed_start, reversed_end = reverse_list(start)

        temp1.next = reversed_start
        reversed_end.next = temp2

        return dummy_node.next

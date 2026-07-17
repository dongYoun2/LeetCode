# submission: https://leetcode.com/problems/rotate-list/submissions/2071438805/
# runtime: 0 ms (beats 100.00%), memory: 19.29 MB (beats 75.87%)
# 12 min
# solved using the rotation trick: right rotation by k == the last k nodes move to the front (same as the "04_19_2025.py". refer to that for the complexity analysis.)


# the key trick is to find the k-th node from the end (technically, (k+1)-th from the end since we need to cut the link between the k-th and (k+1)-th nodes). once we concatenate the tail and the head nodes, the k-th and (k+1)-th node becomes the new head and new tail of the rotated list, respectively.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        n = 1   # the number of nodes
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
        
        k %= n
        if k == 0:  # no rotation needed
            return head

        new_tail = head
        for _ in range(n-k-1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        tail.next = head

        return new_head

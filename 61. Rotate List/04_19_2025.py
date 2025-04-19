# problem: https://leetcode.com/problems/rotate-list/
# submission: https://leetcode.com/problems/rotate-list/submissions/1611692860/

# 20 min
# TC: O(n + n) -> O(n), where n is the number of nodes in the linked list (two passes)
# SC: O(1)

# From LeetCode Top Interview 150 - Linekd List

# It wasn't too difficult as long as I could find the k-th node from the end of the list. I learned the technique where you use two pointers (`ahead` and `behind`) to find the k-th node from problem "19. Remove Nth Node From End of List". One point to consider is that since `k` can be greater than the length of the list, I need to find the length of the list first and then take `k` modulo the length of the list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return None

        node_cnt = 0
        ptr = head
        while ptr is not None:  # find length of linked list
            ptr = ptr.next
            node_cnt += 1

        k %= node_cnt
        ahead = behind = head
        for _ in range(k):
            ahead = ahead.next

        while ahead.next is not None:
            ahead = ahead.next
            behind = behind.next

        ahead.next = head
        new_head = behind.next
        behind.next = None

        return new_head

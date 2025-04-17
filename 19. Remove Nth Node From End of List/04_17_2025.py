# problem: https://leetcode.com/problems/linked-list-cycle/
# submission: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1609496566/

# 9 min
# TC: O(n + n) -> O(n), where n is the number of nodes in the linked list (two-pass alg.)
# SC: O(1)

# From LeetCode Top Interview 150 - Linekd List

# The problem was not too difficult. I solved it in two passes; first, I counted the number of nodes in the linked list, and then I traversed the list again to find the node just before the one I wanted to remove. I checked `if sz == n` to check if I needed to remove the first node. Instead of handling it like the exception case, this can be removed by adding a dummy node at the beginning of the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0

        curr = head
        while curr:
            curr = curr.next
            sz += 1

        if sz == n:   # removing the first node
            return head.next

        cnt = sz - n - 1
        find = head    # finds node right before the node to remove
        while cnt > 0:
            find = find.next
            cnt -= 1

        assert find.next is not None
        find.next = find.next.next

        return head
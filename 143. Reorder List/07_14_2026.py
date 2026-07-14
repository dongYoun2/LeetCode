# submission: https://leetcode.com/problems/reorder-list/submissions/2067750345/
# runtime: 5139 ms (beats 5.08%), memory: 28.86 MB (beats 5.23%)
# 19 min
# solved with recursion, but not optimal in terms of time and space complexity. 

# TC: O(n + n-1 + n-2 + ... + 1) = O(n^2)
# SC: O(n) (recursion stack)


# i simulated the process of reordering the linked list. first, i needed to find the penultimate and last nodes to unlink/link properly with the head node. then, for the second node, i needed to find the penultimate node and the one before it (in terms of the entire linked list). however, since the penultimate node is already unlinked with the last node in the previous step, penultimate node is the last node of the remaining linked list. in this perspective, we can see the recursive structure: "For every node at the front, I need the penultimate and last nodes next." so, i implemented this logic with the recursive function (actually, topic tag includes "recursion"). though the idea is clever, the downside is that this algorithm is not scalable since it takes O(n^2) time.

# cf.) the optimal solution (O(n) time and O(1) space) can be found in the Editorial section. to give a brief overview, this problem is simply a compbination of below three linked list subproblems:
# 1. find the middle node and split into two halves
# 2. reverse the second half
# 3. merge two lists alternately


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reorder(head):
            assert head
            # either single node or two nodes already linked properly (at the end)
            if head.next is None or head.next.next is None:
                return
            
            prev = head
            curr = head.next
            while curr.next is not None:
                prev = curr
                curr = curr.next
            
            next_head = head.next
            head.next = curr

            prev.next = None
            curr.next = next_head

            reorder(next_head)
        
        assert head
        reorder(head)

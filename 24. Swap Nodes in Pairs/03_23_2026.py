# submission: https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1956626632/
# runtime: 0 ms (beats 100.00%), memory: 19.15 MB (beats 95.96%)
# 22 min

# TC: O(n), where n is the number of nodes in the linked list
# SC: O(1)


# this is a typical linked list problem. sometimes, linked list problems are confusing, particularly when we need to unlink and link nodes frequently.

# i approached by setting `prev` and `curr` to the previous node of the first node to swap and the second node to swap itself, respectively. i first simulated with pen and paper for the swapping logic, then coded it up. after swapping, i need to move the `prev` and `curr` pointers to the next state, but since `curr` should be the second node to swap, when there are even number of nodes, we cannot proceed to the `curr.next.next.next` because `curr.next.next` is already None. so i added a `break` statement to handle this case (the code gets messy).

# however, if we set `curr` to the first node to swap (while keeping `prev` the same), the code becomes much cleaner (submission: https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1956633624/). moreover, in a while loop, if we can initialize variables explicitly, such as `first` and `second` to the first and second nodes to swap in addition to `prev` and `curr`, the code becomes even more readable (submission: https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1956638449/); this is exactly the same as the Editorial's "Approach 2: Iterative Approach" section.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        dummy = prev = ListNode(-1, head)
        curr = head.next

        while curr is not None:
            prev.next.next = curr.next
            curr.next = prev.next
            prev.next = curr

            prev = prev.next.next

            if curr.next.next is None:  # when even numer of nodes
                break
            curr = curr.next.next.next
        
        return dummy.next

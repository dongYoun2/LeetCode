# problem: https://leetcode.com/problems/two-sum/
# submission: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/1610526445/

# 25 min
# TC: O(n), where n is the number of nodes in the linked list
# SC: O(1)

# From LeetCode Top Interview 150 - Linekd List

# I feel like linked list problems are always quite confusing since I have to consider several edge cases. This problem was one of them. When I'm testing the test cases, I get an error on the first case, where the linked list is [1,2,3,3,4,4,5]. This was due to no "continue" statement in the code below at first; but after logically simulating the code on that case, I could debug it, and this took quite a bit of time.

# Additionally, I have kept three pointers, `prev`, `curr`, and `nxt`. However, this can be optimized to two pointers, `prev` and `curr`, and `curr.next` can work as the `nxt` pointer; thus, after traversing all duplicates, I can just set `prev.next` to `curr.next` where `curr` is the last duplicate node. This optimized code is shown in the LeetCode Editorial section, so for more details, refer to that.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        INVALID_NUM = 101
        dummy = ListNode(INVALID_NUM, head)

        prev = dummy
        curr = head
        nxt = head.next

        while curr and nxt:
            if curr.val == nxt.val:
                while nxt and nxt.val == curr.val:
                    nxt = nxt.next

                curr = nxt
                prev.next = curr
                if nxt: nxt = nxt.next
                continue

            prev = curr
            curr = nxt
            if nxt: nxt = nxt.next

        return dummy.next


# notes while solving:
# D 1 2 3 3 3 3 3 4 5
# 1 2 4 5

# D 1 1 1 2 3
# 2 3

# D 1 2 2 2
# 1

# D 1 2
# 1 2
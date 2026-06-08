# submission: https://leetcode.com/problems/add-two-numbers/submissions/2026768590/
# runtime: 7 ms (beats 25.51%), memory: 19.37 MB (beats 41.80%)
# 11 min
# typical linked list problem

# refer to the "04_15_2025.py" comments for complexity analysis.


# the algorithm is exactly the same as the "04_15_2025.py" solution.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        carrier = 0
        ans_dummy = curr = ListNode(-1)

        while p1 is not None and p2 is not None:
            num = p1.val + p2.val + carrier
            carrier, digit = divmod(num, 10)

            curr.next = ListNode(digit)
            curr = curr.next

            p1 = p1.next
            p2 = p2.next
        
        rest = p1 or p2
        while rest:
            num = rest.val + carrier
            carrier, digit = divmod(num, 10)

            curr.next = ListNode(digit)
            curr = curr.next

            rest = rest.next

        if carrier:
            curr.next = ListNode(carrier)

        return ans_dummy.next

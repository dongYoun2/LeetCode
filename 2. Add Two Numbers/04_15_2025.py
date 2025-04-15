# problem: https://leetcode.com/problems/add-two-numbers/
# submission: https://leetcode.com/problems/add-two-numbers/submissions/1607668361/

# 14 min
# TC: O(max(m, n)), where m and n are the lengths of the two linked lists.
# SC: O(1) (since the answer space is not counted. If counted, the SC is O(max(m, n) + 1), and plus 1 for the dummy node)

# From LeetCode Top Interview 150 - Linekd List

# It wasn't too tricky. It was just simulating the addition operation of two numbers with linked lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2

        ans = ListNode()    # dummy node
        ans_ptr = ans
        carry = 0
        while ptr1 is not None and ptr2 is not None:
            num = ptr1.val + ptr2.val + carry
            carry, sum_ = divmod(num, 10)

            ans_ptr.next = ListNode(sum_)
            ans_ptr = ans_ptr.next

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        temp = ptr1 if ptr1 is not None else ptr2   # remaining upper digits
        while temp is not None:
            num = temp.val + carry
            carry, sum_ = divmod(num, 10)

            ans_ptr.next = ListNode(sum_)
            ans_ptr = ans_ptr.next

            temp = temp.next

        if carry != 0:  # check last carry
            ans_ptr.next = ListNode(carry)

        return ans.next

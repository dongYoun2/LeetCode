# submission: https://leetcode.com/problems/palindrome-linked-list/submissions/1783818507/
# runtime: 64 ms, memory: 30.18 MB
# this solution solves the follow-up question.

# 1 hr 11 min
# TC: O(n), where n is the number of nodes in the linked list.
# SC: O(1)

# the follow-up question requires solving it in O(1) space, so we cannot use the extra space for the array.

# it took much longer than expected. i was stuck at debugging the reversing logic. also, it took quite long on the middle node finding part since i was considering too much about the odd and even cases. i hope i can solve the follow-up question much faster next time.

# cf.) the code below is a little messy. for improved version and more details, refer to the markdown file.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        assert head is not None
        if head.next is None: return True   # one element

        cnt = 0
        curr = head
        while curr is not None:
            curr = curr.next
            cnt += 1

        prev = None
        med = head
        for _ in range(cnt // 2):
            prev, med = med, med.next

        prev.next = None

        if cnt % 2 == 1:
            med = med.next


        def reverse_linked_list(head):
            assert head is not None
            if head.next is None: return head   # one element

            prev = None
            curr = head
            nxt = curr.next
            while nxt is not None:
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt


            return prev


        ptr1 = reverse_linked_list(head)    # reversed first half
        ptr2 = med  # second half


        while ptr1 is not None and ptr2 is not None:
            if ptr1.val != ptr2.val:
                return False

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        assert ptr1 is None and ptr2 is None

        return True
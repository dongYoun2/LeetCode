# submission: https://leetcode.com/problems/palindrome-linked-list/submissions/2118622089/
# runtime: 39 ms (beats 40.43%), memory: 42.18 MB (beats 96.50%)
# 24 min
# Find Middle (with Fast & Slow Pointers) + Reverse Second half (solves Follow-up Question); logic is the same as the one in the README's "Find Middle (with Fast & Slow Pointers) + Reverse Second half (solves Follow-up Question)" section

# refer to the README for a complexity analysis.


# directly approach for the follow-up question. noticed that i can first find the middle node, then reverse the second half, and lastly compare the two halves. i modularized into a function for the first two steps.

# cf.) here, i used `dummy` node. i first tried to find the middle node without using `dummy`, but then i was only able to find the second middle node when the total number of nodes is even, though i wanted to find the first middle node. actually, if i wanted to find the first middle node, i can simply initialize `slow` to `head` and `fast` to `head.next` as mentioned in the README. on top of that, we don't necessarily need to find the first middle node. the reason i wanted to find the first middle node is to "cut" the linked list into two halves, but we can notice that we don't need to do that as shown in the README's solution.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def find_mid(_head):
            slow = fast = _head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        
        def reverse(_head):
            prev = None
            curr = _head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev


        dummy = ListNode(-1, head)
        mid = find_mid(dummy)
        h2 = mid.next
        mid.next = None

        h2 = reverse(h2)

        curr1, curr2 = head, h2
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            
            curr1 = curr1.next
            curr2 = curr2.next
        
        return True

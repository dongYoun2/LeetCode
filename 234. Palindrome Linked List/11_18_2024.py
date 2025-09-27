# submission: https://leetcode.com/problems/palindrome-linked-list/submissions/1456429642/
# runtime: 19 ms, memory: 38.29 MB

# TC: O(n), where n is the number of nodes in the linked list
# SC: O(n) (for the `arr` list)


# From LeetCode Top Interview 150 - Linked List

# i feel like this is the most straightforward approach. we simply store the values in the array, and then check if the array is the same as the reversed array. this requires multiple passes.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        return arr == arr[::-1]

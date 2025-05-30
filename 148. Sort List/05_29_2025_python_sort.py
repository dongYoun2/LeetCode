# submission: https://leetcode.com/problems/sort-list/submissions/1648453641/

# 3 min
# runtime: 26 ms, memory: 32.82 MB
# TC: O(n log n), where n is the number of nodes in the linked list.
# SC: O(2*n) -> O(n). one for the array to store the nodes and the other for Python timsort.


# From LeetCode Top Interview 150 - Divide & Conquer

# This is the easiest way to think of. I actually came up with this solution before implementing the merge sort solution in "05_29_2025.py". The idea is simply to store nodes in the list and sort them using Python's built-in sort function (Timsort algorithm). After sorting, we can link the nodes back together.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None

        arr = []
        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next

        arr.sort(key=lambda e: e.val)

        for i in range(len(arr) - 1):
            arr[i].next = arr[i+1]

        arr[-1].next = None

        return arr[0]

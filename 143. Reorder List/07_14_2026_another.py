# submission: https://leetcode.com/problems/reorder-list/submissions/2067784498/
# runtime: 3 ms (beats 51.85%), memory: 27.72 MB (beats 79.99%)
# 45 min (time includes "07_14_2026.py" solution)
# solved with leveraging arrays (this is usually discouraged for linked list problems)

# TC: O(n)
# SC: O(n) (for the array)


# after submitting the recursion solution ("07_14_2026.py"), i noticed that the runtime is too long. so, i performed the complexity analysis, and realized it's actually O(n^2) time solution. so, i decided to solve in O(n) time. to solve in linear time as well as in constant space, i may need to leverage the linked list properties, but i couldn't come up with the idea. therefore, i simply shifted to use array to store nodes, though i knew it's not encouraged for the linked list problems. 

# i stored all nodes, and link/unlink them using indices accordingly. however, i first missed the `arr[n//2].next = None` line, so keep getting memory limit exceeded error. debugging took some time, due to considering cases for both even and odd number of nodes. it turns out that i can keep the `for` loop logic the same for both cases, and simply assign the middle node's next to `None` at the end, which also works for both cases.

# cf.) as mentioned in the "07_14_2026.py", refer to the Editorial section for the optimal solution (O(n) time and O(1) space).


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
        arr = []
        curr = head
        while curr is not None:
            arr.append(curr)
            curr = curr.next
        
        n = len(arr)
        for i in range(n//2):
            arr[i].next = arr[n-1-i]
            arr[n-1-i].next = arr[i+1]
        
        arr[n//2].next = None

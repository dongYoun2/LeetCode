# submission: https://leetcode.com/problems/sort-list/submissions/2031268534/
# runtime: 41 ms (beats 82.19%), memory: 43.91 MB (beats 13.14%)
# 9 min
# solved with python's built-in sorting

# refer to the "05_29_2025_python_sort.py" for a complexity analysis


# the below solution is very similar to the "05_29_2025_python_sort.py" solution, but "05_29_2025_python_sort.py" is better since it only stores nodes instead of (value, node) tuple pairs.

# however, this approach is not a problem's intention; the purpose is to solve with the merge sort algorithm.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        nodes = []
        while curr is not None:
            nodes.append((curr.val, curr))
            curr = curr.next
        
        nodes.sort(key=lambda e: e[0])

        for i in range(len(nodes)-1):
            nodes[i][1].next = nodes[i+1][1]
        
        nodes[-1][1].next = None

        return nodes[0][1]

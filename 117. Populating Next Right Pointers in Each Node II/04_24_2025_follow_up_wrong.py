# submission: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/1616757579/

# 54 min

# This is the wrong code for the follow-up question. It's easy to notice why the code is wrong if you look at the failed test case. Refer to the submission link for the failed test case.


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return root

        def level_recursive(prev, nxt):
            if prev and nxt:
                prev.next = nxt
                sub_left = sub_right = None

                if prev.right: sub_left = prev.right
                elif prev.left: sub_left = prev.left

                if nxt.left: sub_right = nxt.left
                elif nxt.right: sub_right = nxt.right

                level_recursive(sub_left, sub_right)

            if prev:
                level_recursive(prev.left, prev.right)

            if nxt:
                level_recursive(nxt.left, nxt.right)

        level_recursive(root.left, root.right)

        return root

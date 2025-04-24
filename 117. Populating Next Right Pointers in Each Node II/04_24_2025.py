# problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# submission: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/1616704246/

# 10 min
# runtime: 44 ms, memory: 18.92 MB
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n)

# From LeetCode Top Interview 150 - Binary Tree General

# I noticed that this is a typical level-order traversal problem, where we can solve it by implementing BFS using a queue. The queue data structure requires O(n) space.

# The follow-up question asks to solve it in O(1) space. We can utilize a next pointer to connect the nodes on the same level (each level is simply a linked list) without using a queue (or without any additional space). For more details, refer to the markdown file.

# cf.) I spent 54 minutes solving the follow-up question, but I couldn't find a solution. After looking at the intuition and brief algorithm explanation part of the LeetCode Editorial's Approach 2 (not the code itself), I realized the key idea and was able to implement the code that uses only a constant space.


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

        q = deque([root])
        while q:
            level_size = len(q)

            for i in range(level_size - 1): # connect next
                q[i].next = q[i+1]
            q[-1].next = None   # acutally not needed since all next pointers are None by default

            for _ in range(level_size):
                node = q.popleft()

                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)

        return root

# submission: https://leetcode.com/problems/symmetric-tree/submissions/1629035090/
# runtime: 0 ms, memory: 18.15 MB

# 17 min
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n + n) -> O(n) (queue space, `level_nodes` list)

# This solutuion is for the follow-up quesiton. I solved it with iterative approach using a queue.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        assert root is not None

        q = deque([root])
        while q:
            level_nodes = []
            for _ in range(len(q)):
                node = q.popleft()

                level_nodes.append(node.val if node else None)

                if node:
                    q.append(node.left)
                    q.append(node.right)

            n = len(level_nodes)
            if n == 1: continue # discard root level

            assert n % 2 == 0
            front = level_nodes[:n//2]
            rear = level_nodes[n//2:]

            if front != list(reversed(rear)):
                return False

        return True

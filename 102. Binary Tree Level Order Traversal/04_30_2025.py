# submission: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1622062716/
# runtime: 0 ms, memory: 18.31 MB

# 5 min
# TC: O(n), where n is the number of nodes in the tree.
# SC: O(n)

# From LeetCode Top Interview 150 - Binary Tree BFS

# Typical BFS problem.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        ans = []
        q = deque([root])
        ans.append([root.val])

        while q:
            level_nodes = []
            for _ in range(len(q)):
                curr = q.popleft()

                if curr.left:
                    level_nodes.append(curr.left.val)
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
                    level_nodes.append(curr.right.val)

            if level_nodes:
                ans.append(level_nodes)

        return ans

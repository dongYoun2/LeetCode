# problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# submission: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1627208351/

# 2 min
# TC: O(n), where n is the number of nodes in the tree. We visit each node once.
# SC: O(h), where h is the height of the tree. This is the space used by the recursion stack.

# From LeetCode Top Interview 150 - Binary Tree General

# cf.) This problem can also be solved using an iteartive approach with a stack.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

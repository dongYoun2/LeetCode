# submission: https://leetcode.com/problems/symmetric-tree/submissions/1629025873/
# runtime: 0 ms, memory: 17.87 MB

# 10 min
# TC: O(n), where n is the number of nodes in the tree
# SC: O(h), where h is the height of the tree (recursion stack space)

# From LeetCode Top Interview 150 - Binary Tree General

# In the beginning, I was thinking of prototyping the recursive function with one root parameter; `isSymmetric`. However, I realized that I need to compare two tree nodes at a time, whether they are mirrored or not. So, I definedthe  `is_mirrored_trees` function.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        assert root is not None

        def is_mirrored_trees(r1, r2):
            if r1 is None or r2 is None:
                return r1 == r2

            return r1.val == r2.val and is_mirrored_trees(r1.left, r2.right) and is_mirrored_trees(r1.right, r2.left)

        return is_mirrored_trees(root.left, root.right)

# problem: https://leetcode.com/problems/same-tree/
# submission: https://leetcode.com/problems/same-tree/submissions/1628257380/

# 4 min
# TC: O(min(n, m)), where n and m are the number of nodes in the two trees.
# SC: O(h), where h is the height of the smaller tree. (recursion stack)
# - worst case: h = min(n, m) if the trees are unbalanced.
# - best case: h = log(min(n, m)) if the trees are balanced.

# From LeetCode Top Interview 150 - Binary Tree General


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None: return p == q

        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

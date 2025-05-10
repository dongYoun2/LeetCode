# problem: https://leetcode.com/problems/path-sum/
# submission: https://leetcode.com/problems/path-sum/submissions/1629727616/

# This is a wrong solution.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False

        def dfs(root_, val_sum):
            if root_ is None:
                return val_sum == targetSum

            val_sum += root_.val

            return dfs(root_.left, val_sum) or dfs(root_.right, val_sum)

        return dfs(root, 0)

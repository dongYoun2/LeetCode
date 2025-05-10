# problem: https://leetcode.com/problems/path-sum/
# submission: https://leetcode.com/problems/path-sum/submissions/1629729383/

# 9 min
# runtime: 3 ms, memory: 18.8 MB
# TC: O(n), where n is the number of nodes in the tree
# SC: O(h), where h is the height of the tree (recursion stack)

# From LeetCode Top Interview 150 - Binary Tree General

# I noticed this is a classic DFS problem, and I first solved it with a recursive approach.

# In the beginning, I coded up like in "05_09_2025_wrong.py", which is a wrong solution. It didn't work since the path sum is computed even for the node with a single child, whereas the question requires the path sum to be computed from the root to a leaf node.

# After failing the specific test case, I coded up the following, which now properly checks whether the node is a leaf node or not.


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
            assert root_ is not None

            if root_.left is None and root_.right is None:
                return val_sum == targetSum

            ret_l = ret_r = False
            if root_.left:
                ret_l = dfs(root_.left, val_sum + root_.left.val)

            if root_.right:
                ret_r = dfs(root_.right, val_sum + root_.right.val)

            return ret_l or ret_r

        return dfs(root, root.val)

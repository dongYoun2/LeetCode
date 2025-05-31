# submission: https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/1650045614/

# 48 min
# TC: O(n), where n is the number of nodes in the tree.
# SC: O(h), where h is the height of the tree (recursion stack space).
# - In a balanced tree, h is O(log n).
# - In a skewed tree, h is O(n).


# From LeetCode Top Interview 150 - Binary Tree General

# The code below implements a tree DP solution using a post-order DFS. The core idea is that the global solution can be computed using local solutions from the left and right subtrees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        assert root is not None

        def max_path_sum(root):
            if root is None:
                return -float('inf'), -float('inf')

            left_max, left_start_max = max_path_sum(root.left)
            right_max, right_start_max = max_path_sum(root.right)

            root_start_left_max = max(root.val, root.val + left_start_max)
            root_start_right_max = max(root.val, root.val + right_start_max)

            root_passing_max = root.val
            if left_start_max > 0:
                root_passing_max += left_start_max
            if right_start_max > 0:
                root_passing_max += right_start_max

            max_path = max(left_max, right_max, root_passing_max)
            root_start_max_path = max(root_start_left_max, root_start_right_max)

            return max_path, root_start_max_path


        return max_path_sum(root)[0]

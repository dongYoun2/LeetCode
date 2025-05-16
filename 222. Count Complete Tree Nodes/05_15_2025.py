# problem: https://leetcode.com/problems/count-complete-tree-nodes/
# submission: https://leetcode.com/problems/count-complete-tree-nodes/submissions/1635213208/

# 4 min
# TC: O(n), where n is the number of nodes in the tree.
# SC: O(h), where h is the height of the tree (for the recursion stack).

# From LeetCode Top Interview 150 - Binary Tree General


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def helper_count(root_):
            if root_ is None: return 0

            l_cnt = helper_count(root_.left)
            r_cnt = helper_count(root_.right)

            return l_cnt + r_cnt + 1

        return helper_count(root)

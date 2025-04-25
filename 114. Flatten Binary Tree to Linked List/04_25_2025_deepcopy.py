# problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# submission: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/1617750634/

# 5 min
# TC: O(n + n) -> O(n), where n is the number of nodes in the tree (deepcopy + recursion stack)
# SC: O(n + n) -> O(n) (deepcopy + recursion stack)

# From LeetCode Top Interview 150 - Binary Tree General


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import copy

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return root

        root_cp = copy.deepcopy(root)

        def preorder(root_):
            if root_ is not None:
                nonlocal ptr, prev
                if ptr:
                    ptr.val = root_.val
                else:
                    ptr = TreeNode(root_.val)
                    assert prev is not None
                    prev.right = ptr

                ptr.left = None
                prev = ptr
                ptr = ptr.right

                preorder(root_.left)
                preorder(root_.right)

        prev = None
        ptr = root
        preorder(root_cp)

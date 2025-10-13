# this is a wrong solution

# 45 min

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder_cp(root_, parent_cp, is_left_child):
            if root_ is not None:
                if is_left_child:
                    parent_cp.left = TreeNode(root_.val)
                    preorder_cp(root_.left, parent_cp.left, True)
                    preorder_cp(root_.right, parent_cp.left, False)
                else:
                    parent_cp.right = TreeNode(root_.val)
                    preorder_cp(root_.left, parent_cp.right, True)
                    preorder_cp(root_.right, parent_cp.right, False)


        def preorder(root_):
            if root_ is not None:
                nonlocal ptr
                if ptr:
                    ptr.right = TreeNode(root_.val)

                    ptr.left = None
                    ptr = ptr.right

                preorder(root_.left)
                preorder(root_.right)


        dummy = TreeNode(-101)
        preorder_cp(root, dummy, False)

        if root:
            root.left = None
            ptr = root.right

        preorder(dummy.right)

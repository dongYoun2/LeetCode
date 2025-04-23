# problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# submission: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1614737196/ (Runtime: 31 ms)

# TC: O(n), where n is the number of nodes in the tree
# SC: O(n)

# I simply converted "04_22_2025.py" to pass indices as arguments instead of slices. In Python, slicing the list makes a copy of the list, which requires additional linear time and space. By passing the indices, we can avoid this overhead. The execution time became 3x faster than the "04_22_2025.py" code.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper_build_tree(pre_s, pre_e, in_s, in_e):
            if in_e - in_s < 0: return None

            val = preorder[pre_s]
            pos = inorder.index(val, in_s, in_e + 1)
            left_len = pos - in_s

            left = helper_build_tree(pre_s + 1, pre_s + left_len, in_s, pos - 1)
            right = helper_build_tree(pre_s + 1 + left_len, pre_e, pos + 1, in_e)

            return TreeNode(val, left, right)

        return helper_build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)

# submission: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1614737196/
# runtime: 31 ms (beats 54.24%), memory: 19.16 MB (beats 87.36%)

# TC: O(n^2), where n is the number of nodes in the tree (worst-case: skewed tree)
# - this is for the search operation in the `index` method across all recursive calls
# SC: O(h), where h is the height of the tree (worst-case: skewed tree: h == n, best-case: balanced tree: h == log n); 
# - this is for the recursion stack

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

# submission: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1614624113/
# runtime: 96 ms (beats 19.14%), memory: 89.12 MB (beats 32.61%)

# 19 min
# TC: O(n^2 + n^2) -> O(n^2), where n is the number of nodes in the tree (worst-case: skewed tree)
# - O(n^2) for search and O(n^2) for slicing
# SC: O(h + n^2) -> O(n^2), where h is the height of the tree
# - O(h): recursion stack space; worst-case (skewed tree): h == n, best-case (balanced tree): h == log n
# - O(n^2): list slicing (copying) across all recursive calls

# From LeetCode Top Interview 150 - Binary Tree General

# I think the core idea is to use the preorder traversal to find the root of the tree and then use the inorder traversal to find the left and right subtrees.

# The below code can further be optimized by:
# 1. Passing indices instead of slices to avoid copying the list, which requires additional linear time and space.
# 2. Using a dictionary to store the indices of the inorder traversal at once as a preprocessing step, so that we can avoid the linear search for the index of the root in the inorder list every time we call the function.

# After submitting the "04_22_2025.py" solution, I optimized it with the above first point, and coded up on the "04_22_2025_passing_indices.py" (31 ms runtime). I couldn't think of the second point at that moment, and found it out after going through LeetCode's Editorial section. By applying both optimizations, the execution time was reduced significantly compared to applying only the first optimization technique ("04_22_2025_passing_indices.py"). Refer to the markdown filw for the code with both optimizations.

# cf.) I just realized that the `right_len` variable is not used in the code, and `left_len` is simply `pos` haha.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) <= 0: return None

        val = preorder[0]
        pos = inorder.index(val)
        left_len = pos
        right_len = len(inorder) - left_len - 1

        left = Solution.buildTree(self, preorder[1:1+left_len], inorder[:pos])
        right = Solution.buildTree(self, preorder[1+left_len:], inorder[pos+1:])

        return TreeNode(val, left, right)

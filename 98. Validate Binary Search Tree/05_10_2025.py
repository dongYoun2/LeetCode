# submission: https://leetcode.com/problems/validate-binary-search-tree/submissions/1630460928/
# runtime: 3 ms, memory: 20.3 MB

# 5 min
# TC: O(n + n log n) -> O(n log n), where n is the number of nodes in the tree (inorder traversal + sorting)
# SC: O(n + n) -> O(n) (for `inorder_arr` list and sorted list to compare)

# From LeetCode Top Interview 150 - Binary Tree General

# In a valid BST, its inorder traversal should yield a sorted array. So the idea is simply to see whether the inorder traversal is sorted. Notice that since all values in BST have to be unique by the pure textbook definition of BST, which is equivalent to the BST definition introduced in this question, we need to remove duplicates using `set` before sorting, then compare with the original inorder traversal array.

# cf.) There's another approach using recursion to check whether the current node's value is within the valid range. For more details, refer to the markdown file.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        assert root is not None
        inorder_arr = []

        def inorder(root_):
            if root_ is not None:
                inorder(root_.left)
                inorder_arr.append(root_.val)
                inorder(root_.right)

        inorder(root)

        return inorder_arr == sorted(set(inorder_arr))

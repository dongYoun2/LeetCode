# submission: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/1653267186/

# 5 min
# TC: O(n), where n is the number of elements in the input array. Each element is processed once to create a node in the BST.
# SC: O(h) -> O(log n) where h is the tree height. In this case, the tree is balanced. (For recursion stack space)

# From LeetCode Top Interview 150 - Divide & Conquer


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        assert nums


        def build_bst(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            val = nums[mid]

            left_child = build_bst(left, mid - 1)
            right_child = build_bst(mid + 1, right)

            root = TreeNode(val, left_child, right_child)

            return root


        return build_bst(0, len(nums) - 1)

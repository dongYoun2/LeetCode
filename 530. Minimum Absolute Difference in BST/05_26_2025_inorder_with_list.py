# submission: https://leetcode.com/problems/minimum-absolute-difference-in-bst/submissions/1645443645/

# 6 min
# TC: O(n), where n is the number of nodes in the tree. (inorder traversal + one loop for finding the minimum difference)
# SC: O(h), where h is the height of the tree. (recursion stack)

# From LeetCode Top Interview 150 - Binary Search Tree


# After attempting with the "05_26_2025.py", I realized that I can also find the sorted order of the values in BST by doing an inorder traversal, then finding the minimum absolute difference by comparing adjacent values. This approach is easier to implement and more efficient in terms of time complexity than the "05_26_2025.py" solution since it avoids the need to find predecessors and successors for each node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ordered_nums = []
        def inorder(node):
            if node is None: return

            inorder(node.left)
            ordered_nums.append(node.val)
            inorder(node.right)


        inorder(root)

        assert len(ordered_nums) >= 2

        ans = float('inf')
        for i in range(1, len(ordered_nums)):
            ans = min(ans, ordered_nums[i] - ordered_nums[i-1])

        return ans

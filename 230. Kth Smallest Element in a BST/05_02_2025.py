# problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# submission: https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/1623595448/

# 10 min
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n) (recursion stack)

# From LeetCode Top Interview 150 - Binary Tree BFS

# follow-up questions include "701. Insert into a Binary Search Tree" and "450. Delete Node in a BST".


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        assert root is not None

        ans = -1
        cnt = 0
        def search(root_):
            if root_ is None: return

            nonlocal cnt, ans

            search(root_.left)

            cnt += 1
            if cnt == k:
                ans = root_.val
                return

            search(root_.right)

        search(root)

        return ans

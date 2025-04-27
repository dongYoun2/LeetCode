# problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# submission: https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/1618942818/

# 8 min
# runtime: 0 ms, memory: 17.84 MB
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n) (recursion stack)

# From LeetCode Top Interview 150 - Binary Tree General

# After solving the problem using BFS, I also implemented the DFS solution here.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root_, num):
            if not root_.left and not root_.right:
                nonlocal ans
                ans += num

            if root_.left:
                dfs(root_.left, 10 * num + root_.left.val)

            if root_.right:
                print(num)
                dfs(root_.right, 10 * num + root_.right.val)

        assert root is not None
        dfs(root, root.val)

        return ans

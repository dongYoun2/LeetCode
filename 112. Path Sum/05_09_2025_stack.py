# problem: https://leetcode.com/problems/path-sum/
# submission: https://leetcode.com/problems/path-sum/submissions/1629746290/

# 6 min (attempted after solving the recursive version "05_09_2025.py")
# runtime: 0 ms, memory: 19.1 MB
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n) (stack data structure space)

# Below is a simple iterative DFS solution using a stack.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False

        stack = deque([(root, root.val)])
        while stack:
            curr, curr_sum = stack.pop()

            if curr.left is None and curr.right is None:
                if curr_sum == targetSum:
                    return True

                continue

            if curr.right:
                stack.append((curr.right, curr_sum + curr.right.val))

            if curr.left:
                stack.append((curr.left, curr_sum + curr.left.val))

        return False

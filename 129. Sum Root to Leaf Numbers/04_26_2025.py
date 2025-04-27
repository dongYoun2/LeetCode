# problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# submission: https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/1618942818/

# 13 min
# runtime: 0 ms, memory: 17.83 MB
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n + n) -> O(n) (n for storing node and n for storing constructing number)

# From LeetCode Top Interview 150 - Binary Tree General

# I used BFS (level-order traversal) to solve this problem since that was the first approach that came to my mind, but shortly after, I also noticed that DFS would also work. After submitting the BFS solution, I implemented the DFS solution in the "04_26_2025_dfs.py" file as well.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        assert root is not None

        ans = 0
        q = deque([(root, root.val)])

        while q:
            node, num = q.popleft()

            if node.left:
                next_num = 10 * num + node.left.val
                q.append((node.left, next_num))

            if node.right:
                next_num = 10 * num + node.right.val
                q.append((node.right, next_num))

            if not node.left and not node.right:
                ans += num


        return ans

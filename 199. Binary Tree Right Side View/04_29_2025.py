# problem: https://leetcode.com/problems/binary-tree-right-side-view/
# submission: https://leetcode.com/problems/binary-tree-right-side-view/submissions/1621590619/

# 7 min
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n)

# From LeetCode Top Interview 150 - Binary Tree BFS

# Simple BFS or level order traversal problem.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        ans  = []
        q = deque([root])

        while q:
            q_size = len(q)
            last_idx = q_size - 1

            for i in range(q_size):
                curr = q.popleft()

                if i == last_idx:
                    ans.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return ans

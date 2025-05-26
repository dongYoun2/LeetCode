# submission: https://leetcode.com/problems/average-of-levels-in-binary-tree/submissions/1645418118/

# 6 min
# TC: O(V+E) -> O(V+(V-1)) -> O(v), where V is the number of nodes and E is the number of edges. In the case of binary trees, E is V-1 since each node (except the root) has exactly one parent.
# SC: O(W), where W is the maximum width of the tree, which is the maximum number of nodes at any level.

# From LeetCode Top Interview 150 - Binary Tree BFS

# This is a typical BFS problem.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        assert root is not None

        q = deque([root])
        answers = []

        while q:
            total = 0.0
            cnt = 0
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val
                cnt += 1

                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)

            avg = total / cnt
            answers.append(avg)

        return answers

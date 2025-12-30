# submission: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1869776500/
# runtime: 0 ms, memory: 18.24 MB

# 5 min
# TC: O(n)
# SC: O(n)

# used queue and performed BFS.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        ans = []
        q = deque([root])
        while q:
            children = []
            for _ in range(len(q)):
                node = q.popleft()
                children.append(node.val)

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            ans.append(children)

        return ans

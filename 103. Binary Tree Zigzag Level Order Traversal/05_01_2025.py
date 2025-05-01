# problem: https: // leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# submission: https: // leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/1622741355/

# 17 min
# TC: O(n), where n is the number of nodes in the tree.
# SC: O(n)

# From LeetCode Top Interview 150 - Binary Tree BFS

# At first, I simply changed the order of appending the nodes to the queue depending on the `backward` variable, but this is the wrong approach. It doesn't work for the case where the tree is "[1,2,3,4,null,null,5]". (Wrong submission: https: // leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/1622734839/)

# After debugging the above case, I kept the order of appending the nodes to the queue the same, but changed the order of reading the nodes from the queue.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        ans = []
        q = deque([root])
        backward = False

        while q:
            if backward:
                level_nodes = [e.val for e in list(q)[::-1]]
            else:
                level_nodes = [e.val for e in q]

            ans.append(level_nodes)
            backward = not backward

            for _ in range(len(q)):
                node = q.popleft()

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return ans


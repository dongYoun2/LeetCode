# submission: https://leetcode.com/problems/inorder-successor-in-bst/submissions/2021645026/
# runtime: 76 ms (beats 5.08%), memory: 22.93 MB (beats 16.05%)
# 23 min

# TC: O(n), where n is the number of nodes in the tree
# SC: O(n) (two arrays)


# this would be considered as a brute force solution. i mantinaed arrays to store the values and nodes themselves in the order of inorder traversal. then, i simply found the index of the target value and returned the next node.

# cf.) this is a naive solution and not actually a purpose of this problem. refer to the README.md for the optimal solution.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        nodes = []
        vals = []

        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                vals.append(node.val)
                inorder(node.right)
        
        inorder(root)
        assert len(nodes) == len(vals)

        find = vals.index(p.val)

        return nodes[find+1] if find < len(nodes) - 1 else None

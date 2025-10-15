# submission: https://leetcode.com/problems/symmetric-tree/submissions/1802361992/
# runtime: 0 ms, memory: 17.9 MB

# 13 min
# TC: O(n), where n is the number of nodes in the tree
# SC: O(h), where h is the height of the tree


# felt a little tricky at first, but quite straightforward once you think of how to compare whether two trees are mirrored or not recursively.

# cf.) it would be slightly better to use `return node1 == node2` instead of `return node1 is node2` in the `is_mirrored` function.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        assert root

        def is_mirrored(node1, node2):
            if not node1 or not node2: return node1 is node2
            return node1.val == node2.val  \
                and is_mirrored(node1.left, node2.right) \
                and is_mirrored(node1.right, node2.left)

        return is_mirrored(root.left, root.right)

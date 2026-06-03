# submission: https://leetcode.com/problems/inorder-successor-in-bst/submissions/2021647700/
# runtime: 60 ms (beats 74.43%), memory: 22.84 MB (beats 36.36%)
# 26 min

# TC: O(n), where n is the number of nodes in the tree
# SC: O(h), where h is the height of the tree (recursion stack)
# - average: h = log n
# - worst: h = n


# this is a somewhat better solution than the "06_03_2026.py". it is still based on the inorder traversal, but doesn't store the entire nodes and values in the array. so the space complexity is O(h), though in worst case, it is O(n).

# cf.) this is still not an optimal solution. refer to the README.md for that.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        ans = None
        found = False

        def inorder(node):
            nonlocal ans, found
            if node:
                inorder(node.left)
                if node.val > p.val and not found:
                    found = True
                    ans = node
                inorder(node.right)
        
        inorder(root)
        return ans

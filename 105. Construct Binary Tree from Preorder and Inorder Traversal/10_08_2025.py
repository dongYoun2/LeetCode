# submission: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1795356617/
# runtime: 101 ms (beats 16.46%), memory: 89.22 MB (beats 32.19%)
# 13 min

# time and space complexity are identical to the "04_22_2025.py" solution.

# refer to the "04_22_2025.py" for the detailed comments, and markdown file for the most efficient solution.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        assert preorder

        def build(preorder, inorder):
            if not preorder:
                return None

            root_val = preorder[0]

            left_cnt = inorder.index(root_val)

            left = build(preorder[1:1+left_cnt], inorder[:left_cnt])
            right = build(preorder[1+left_cnt:], inorder[left_cnt+1:])

            return TreeNode(root_val, left, right)


        return build(preorder, inorder)


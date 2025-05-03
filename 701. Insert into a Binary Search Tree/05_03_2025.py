# problem: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# submission: https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/1624378041/

# 6 min
# TC: O(h), where h is the height of the tree
# SC: O(h) (for recursion stack)

# 230. Kth Smallest Element in a BST's follow-up question is "If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?", and I found this BST insertion question in LeetCode. I think it is good to review before thinking about 230's follow-up question, so I solved this one first.

# cf.) Iterative approach reduces the recursion stack space, which allows the space complexity to be O(1). For this approach, refer to the Editorial section.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

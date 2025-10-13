# submission: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/1798445522/
# runtime: 0 ms, memory: 17.95 MB

# 24 min
# TC: O(n^2) (skewed tree: worst-case), and O(n log n) (balanced tree), where n is the number of nodes in the tree
# - the time complexity can be optimized to O(n)
# SC: O(n), for the recursion stack


# i thought in two steps to flatten the tree:
# 1. node.right, node.left = node.left, None: this connects the left subtree to the right child
# 2. node.(prev)_left.rightmost_node.right = node.(prev)_right: this connects the original right subtree (before step 1) to the rightmost node of the original left subtree

# i implemented it in a recursive manner. however, i implemented the second step in a while loop (O(n) time), leading the entire time complexity to be O(n^2). however, as mentioned above, this can be further optimized to O(n) by using a tail pointer. for more details, refer to the markdown file.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None

        def recur_flatten(node):
            if node.left:
                prev_right = node.right # could be null
                node.right, node.left = node.left, None

                # finding prev left subtree's rightmost node
                right_most_node = node.right
                while right_most_node.right:
                    right_most_node = right_most_node.right

                right_most_node.right = prev_right

            if node.right:
                recur_flatten(node.right)


        recur_flatten(root)

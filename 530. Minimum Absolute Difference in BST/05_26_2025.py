# submission: https://leetcode.com/problems/minimum-absolute-difference-in-bst/submissions/1645439892/

# 18 min
# TC: O(n * 2h) -> O(n*h), where n is the number of nodes in the tree and h is the height of the tree.
# - O(n): for preorder traversal.
# - O(2h): for finding the predecessor and successor of each node.
# SC: O(h) (recursion stack)

# From LeetCode Top Interview 150 - Binary Search Tree

# This is the code for my first attempt. By thinking of the featuer of BST—the largest value that is smaller than the current node is the rightmost node of the left subtree, and the smallest value that is larger than the current node is the leftmost node of the right subtree—I was able to find the predecessor and successor, which are the candidates for the minimum absolute difference with the current node. I could find the answer by visiting every node in the tree with a preorder traversal.

# I also thought there may be a better solution since finding the predecessor and successor of each node seems inefficient and redundant, but my plan was to get this solution working first and then consider a better approach.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def get_node_min_diff(node):
            assert node is not None

            diff = float('inf')

            if node.left:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right

                diff = min(diff, abs(node.val - predecessor.val))

            if node.right:
                successor = node.right
                while successor.left:
                    successor = successor.left

                diff = min(diff, abs(node.val - successor.val))

            return diff

        ans = float('inf')


        def preorder(node):
            nonlocal ans
            if node is None: return
            if ans == 1: return

            diff = get_node_min_diff(node)
            ans = min(ans, diff)

            preorder(node.left)
            preorder(node.right)


        preorder(root)
        return ans

# submission: https://leetcode.com/problems/subtree-of-another-tree/submissions/1785913006/
# runtime: 45 ms, memory: 18.1 MB

# 20 min
# TC: O(m * n), where m and n are the number of nodes in the two trees.
# SC: O(m + n) (worst case)


# the key is to find the root of the subtree while traversing the main tree. the code below does DFS (`find()` function) for traversing. To do this, we need to check if the tree rooted at the current node is the same as the `subRoot` tree (`is_equal()` function).

# The code below is a little verbose. Improved version can be found in the markdown file.

# cf.) The time complexity can be optimized to O(m+n) using the string representation of the trees. More details can be also found in the markdown file.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_equal(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None:
                return False

            return r1.val == r2.val and is_equal(r1.left, r2.left) and is_equal(r1.right, r2.right)


        def find(root):
            if root is None: return False

            if root.val == subRoot.val:
                if is_equal(root, subRoot):
                    return True

            if find(root.left):
                return True

            if find(root.right):
                return True

            return False


        return find(root)

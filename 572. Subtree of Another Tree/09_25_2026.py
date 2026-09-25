# submission: https://leetcode.com/problems/subtree-of-another-tree/submissions/2153360428/
# runtime: 43 ms (beats 43.53%), memory: 19.85 MB (beats 39.78%)
# 13 min
# solved uisng DFS (the logic is the same as the 1) 09_29_2025.py or 2) README.md's "Using DFS" approach)

# complexity analysis is the same as the two solutions mentioned above.


# always good to think of recursion for tree problems since the definition of a tree is inherently recursive.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        assert root and subRoot

        def is_same(r1, r2):
            if r1 is None or r2 is None:
                return r1 == r2

            return r1.val == r2.val and is_same(r1.left, r2.left) and is_same(r1.right, r2.right)


        def is_subtree(r):
            if is_same(r, subRoot):
                return True

            if r is not None:
                if is_subtree(r.left):
                    return True

                if is_subtree(r.right):
                    return True

            return False


        return is_subtree(root)

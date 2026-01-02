# submission: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1870719344/
# runtime: 58 ms, memory: 21.53 MB

# 43 min
# refer to the README.md for the complexity analysis.

# unlike previous attempts (04_28_2025.py, 10_14_2025.py), the code below is the most concise and standard way to solve this problem. the logic exactly matches with the README's solution.

# however, it took much longer to solve than expected. 'Grind 128 questions' shows 25 minutes as the desired time.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find(node):
            if node is None:
                return None

            if node is p or node is q:
                return node

            a, b = find(node.left), find(node.right)

            if a and b:
                return node
            elif a or b:
                return a or b

        return find(root)

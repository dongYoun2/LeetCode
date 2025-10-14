# submission: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1801578583/
# runtime: 60 ms, memory: 22.57 MB

# 35 min
# TC: O(n), where n is the number of nodes in the tree
# SC: O(h), where h is the height of the tree
# - skewed tree (worst case): h = n
# - balanced tree : h = log n


# took a while to solve this proble. felt a bit tricky (just as the last time lol). though i solved it in 35 minutes, i don't think i wrote the code while thinking logically, and step by step.

# the main idea of this solution is to post-order traverse the tree, and when the current node is the LCA, we set the `ans` to the current node. to do this i defined the recursive function `find()` to return two boolean values: whether p and q are found in the given subtree.

# however, the code is very verbose. it can be further simplified and optimized (early returning if the `ans` is already set). the improved version of this approach can be found at: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1801714487/ (runtime: 50 ms, memory: 22.40 MB)

# also, instead of the recursive function to return two boolean values, we can implement by directly returning the (potential) LCA node if found or `None` otherwise. for more details, refer to the markdown file.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        assert (p is not q) and root

        ans = None
        def find(node):
            if not node: return False, False

            p_left_found, q_left_found = find(node.left)
            p_right_found, q_right_found = find(node.right)

            nonlocal ans
            if not ans:
                if p_left_found and q_left_found:
                    ans = node.left
                elif p_right_found and q_right_found:
                    ans = node.right
                elif (p_left_found and q_right_found) or (p_right_found and q_left_found):
                    ans = node

            p_found = p_left_found or p_right_found
            q_found = q_left_found or q_right_found

            if node is p:
                if not ans and q_found:
                    ans = node
                return True, q_found
            if node is q:
                if not ans and p_found:
                    ans = node
                return p_found, True

            return p_found, q_found


        find(root)
        return ans


# notes while solving problem:
# if p is ancestor of q: return p
# if q is ancestor of p: return q

# while post-order traversal:
#     if node is ancestor of both p and q:
#         return node

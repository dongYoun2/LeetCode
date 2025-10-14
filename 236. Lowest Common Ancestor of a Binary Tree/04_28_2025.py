# submission: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1620437522/

# 36 min
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n)

# From LeetCode Top Interview 150 - Binary Tree General

# Felt a little bit tricky due to the nature of the tree data structure that a child node cannot go back to the parent node. However, this could be solved by using recursion. I used DFS to find the lowest common ancestor (LCA) of two nodes in a binary tree. The algorithm is as follows:

# 1. Recursively call `dfs` on the left and right children of the node.
# - 1. If both left and right children return non-`None` nodes, it means the current node is the LCA, so return it.
# - 2. If only one of the left or right children returns a non-`None` node, check if the current node matches either `p` or `q`. If it does, return the current node since it is the LCA. Otherwise, return the non-`None` child.
# - 3. If both left and right children return `None`, check if the current node matches either `p` or `q`. If it does, return the current node to push it up to the parent node. Otherwise, return `None`.

# I spent for a while to debug since I just returned `None` when both left and right children returned `None`, which doesn't push the current node even if it matches either `p` or `q`.

# cf.)
# After solving it, I realized that this problem can be more easily solved by:
# 1. directly comparing nodes rather than the values of nodes.
# 2. Checking if the current node is `p` or `q` before calling `dfs` on the left and right children.
# This way, we can make the code cleaner and avoid unnecessary recursive calls. For more details, refer to the markdown file.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        assert p is not None and q is not None
        assert p is not q

        def dfs(root_):
            if root_ is None: return None

            l_node = dfs(root_.left)
            r_node = dfs(root_.right)

            if l_node and r_node:
                return root_
            elif l_node or r_node:
                valid_node = l_node or r_node
                min_, max_ = min(valid_node.val, root_.val), max(valid_node.val, root_.val)
                if min_ == n_min and max_ == n_max:
                    return root_
                else:
                    return valid_node
            else:
                if root_.val == n_min or root_.val == n_max:
                    return root_
                else:
                    return None


        n_min,  n_max = min(p.val, q.val), max(p.val, q.val)
        return dfs(root)

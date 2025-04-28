```python
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

            if (root_ is p) or (root_ is q):
                return root_

            l_node = dfs(root_.left)
            r_node = dfs(root_.right)

            if l_node and r_node:   # p (or q) is in left and q (or p) is in right
                return root_
            else:   # p and q is in either one of trees (left or right)
                return l_node or r_node

        return dfs(root)

```
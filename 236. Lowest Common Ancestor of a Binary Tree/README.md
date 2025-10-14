[Problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## DFS Approach

Explanations are described in the comments below.


- [Submission](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1801613472/) (Runtime: 63 ms, Memory: 22.00 MB)
- TC: $O(n)$, where $n$ is the number of nodes in the tree
- SC: $O(h)$, where $h$ is the height of the tree
- - skewed tree (worst case): $h = n$
- - balanced tree : $h = log n$

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        assert root
        assert p and q
        assert p is not q

        def dfs(node):
            if not node: return None

            if (node is p) or (node is q):
                return node

            left_res = dfs(node.left)
            right_res = dfs(node.right)

            if left_res and right_res:
                # found p and q in different subtrees → current node is their LCA
                return node
            elif left_res or right_res:
                # one of two cases:
                # 1. both p and q are in the same subtree (LCA already computed below)
                # 2. only one of p or q found so far -> propagate upward
                return left_res or right_res
            else:
                return None

        return dfs(root)

```

Exactly the same logic but more concise code (complexities are the same):

- [Submission](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1801684584/) (Runtime: 54 ms, Memory: 22.10 MB)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        assert root
        assert p and q
        assert p is not q

        def dfs(node):
            if (not node) or (node is p) or (node is q):
                return node

            left_res = dfs(node.left)
            right_res = dfs(node.right)

            return node if left_res and right_res else (left_res or right_res)

        return dfs(root)

```
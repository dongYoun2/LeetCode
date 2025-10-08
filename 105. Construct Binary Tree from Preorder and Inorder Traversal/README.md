[Problem](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)


## Recursive Approach with Hash Table

The code below is written by ChatGPT.

- [Submission](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1795368213/) (Runtime: 0 ms, Memory: 19.20 MB)
- TC: $O(n)$, where $n$ is the number of nodes in the tree. (Time Complexity is optimized due to the hash table compared to the `10_08_2025.py` solution.)
- SC: $O(n + n)$ -> $O(n)$, for the hash table and the recursion stack.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        assert preorder

        pos = {v: i for i, v in enumerate(inorder)}  # value -> inorder index
        i = 0  # current root index in preorder

        def build(lo: int, hi: int):
            nonlocal i
            if lo > hi:
                return None
            root_val = preorder[i]; i += 1
            mid = pos[root_val]

            root = TreeNode(root_val)
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)

            return root


        return build(0, len(inorder) - 1)

```
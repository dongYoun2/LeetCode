[Problem](https://leetcode.com/problems/inorder-successor-in-bst/)


Instead of performing an inorder traversal, we can use the BST property directly. Starting from the root, whenever `root.val > p.val`, the current node becomes a candidate successor and we move left to look for a smaller valid successor. Otherwise, we move right since all values in the left subtree are smaller than the current node. The final candidate is the inorder successor.


[Submission](https://leetcode.com/problems/inorder-successor-in-bst/submissions/2021660169/)—Runtime: 61 ms (beats 69.74%), Memory: 22.78 MB (beats 62.07%)

- TC: $O(n)$, where $n$ is the number of nodes in the tree.
- SC: $O(1)$


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None

        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor

```
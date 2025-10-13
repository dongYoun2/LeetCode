[Problem](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

## Recursive Approach

The code below is written by ChatGPT. The algorithm contains three steps:
1. Flatten the left subtree
2. Flatten the right subtree
3. Concatenate the root node, flattened left subtree, and flattened right subtree

This solution can be seen as the optimized version of the `04_25_2025.py` solution. While the `04_25_2025.py` finds the tail of the flattened left subtree by traversing again in a while loop, this solution finds and returns the tail in the recursive function. In words, it returns the tail node on the way back to the root node. This has the advantage of reducing the time complexity from $O(n^2)$ to $O(n)$.

This code and the `04_25_2025.py` code are both **Post-order (bottom-up)** based solutions. Left/right subtrees are flattened first (by the recursion calls), then they are merged with the root node.

- [Submission](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/1798505758/) (Runtime: 2 ms, Memory: 17.96 MB)
- TC: $O(n)$, where $n$ is the number of nodes in the tree.
- SC: $O(n)$ (recursion stack)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def recur_flatten(node) -> Optional[TreeNode]:
            # Returns the tail (rightmost) node of the flattened subtree rooted at `node`
            if not node:
                return None

            left_tail = recur_flatten(node.left)
            right_tail = recur_flatten(node.right)

            if left_tail:
                # Splice: [node] -> [left] -> ... -> [left_tail] -> [right]
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            # Return the rightmost tail after rewiring
            return right_tail or left_tail or node

        recur_flatten(root)

```


## Iterative Approach (Solves the follow-up question)

The code below is also written by ChatGPT. It can be seen as the iterative and optimized version (since the time complexity is reduced) of the `10_11_2025.py` code.

The code below and the `10_11_2025.py` code are both **pre-order (top-down)** based solutions. So, at each node during the traversal, it immediately rewires the left and right subtrees, then keep traversing to the right child.

- [Submission](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/1798493196/) (Runtime: 0 ms, Memory: 18.08 MB)
- TC: $O(n)$
- SC: $O(1)$

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                # find rightmost node of left subtree
                pre = curr.left
                while pre.right:
                    pre = pre.right

                # splice
                pre.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right

```
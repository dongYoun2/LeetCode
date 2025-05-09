[Problem](https://leetcode.com/problems/symmetric-tree/)

## Iteartive Approach with Stack

- [Submission](https://leetcode.com/problems/symmetric-tree/submissions/1629040882/)
- TC: $O(n)$, where $n$ is the number of nodes in the tree.
- SC: $O(n)$ (for the stack space).



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        assert root is not None

        stack = deque()

        stack.append(root.left)
        stack.append(root.right)

        while stack:
            r = stack.pop()
            l = stack.pop()

            if (l is None) and (r is None):
                continue
            if (l is None) or (r is None) or l.val != r.val:
                return False

            stack.append(l.left)
            stack.append(r.right)

            stack.append(l.right)
            stack.append(r.left)

        return True

```
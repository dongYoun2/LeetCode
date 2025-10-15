[Problem](https://leetcode.com/problems/symmetric-tree/)

## Recursive Approach

Please refer to the [`10_15_2025.py`](10_15_2025.py) for the recursive approach.


## Iterative Approach with Queue

Please refer to the [`05_08_2025_follow_up.py`](05_08_2025_follow_up.py) for the iterative approach with queue.


## Iteartive Approach with Stack

- [Submission](https://leetcode.com/problems/symmetric-tree/submissions/1629040882/) (Runtime: 0 ms, Memory: 17.80 MB)
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
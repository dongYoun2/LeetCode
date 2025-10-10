[Problem](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

## Using previously established next pointers

The logic is the same as the LeetCode Editorial's Approach 2. The only difference is that the code below uses a 1) dummy node and 2) a recursive function.

The key idea is that when processing the `N`th level to connect all the nodes on that level, we can ensure that the `N-1` nodes are all connected; the previous level forms a linked list. This allows us to connect the current level nodes while traversing the previous nodes through the linked list. Before, we used a queue data structure (`04_24_2025.py`) to store all the nodes in the next level. Now, since we can guarantee that all current level nodes are reachable by traversing previous level nodes (linked list), we don't need a queue.

**One thing to keep in mind is that since we can only access children nodes from a parent node (or next-level nodes from the previous level), not vice versa (due to the tree structure), we establish the `N+1`th level's `next` pointers while still on the `N`th level.** For more details, refer to the Editorial's second approach.


- [Submission](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/1616977937/) (runtime: 47 ms, memory: 19.1 MB)
- TC: $O(n)$, where $n$ is the number of nodes in the tree
- SC: $O(1)$ (Recursion stack is not considered since it doesn't count as an extra space in the follw-up question.)


```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def level_recursive(leftmost):
            if leftmost is None: return

            ptr = leftmost
            child_prev = dummy = Node(-101)
            while ptr:
                if ptr.left:
                    child_prev.next = ptr.left
                    child_prev = child_prev.next
                if ptr.right:
                    child_prev.next = ptr.right
                    child_prev = child_prev.next

                ptr = ptr.next

            level_recursive(dummy.next)

        level_recursive(root)
        return root

```
# submission: https://leetcode.com/problems/clone-graph/submissions/1869783031/
# runtime: 41 ms, memory: 17.98 MB

# 13 min
# refer to the 05_12_2025.py for the complexity analysis.

# cf.) the code below is very similar to the 05_12_2025.py.

# a key point for this problem is that we need to have to reference of the cloned nodes; for this, i kept a dictionary where key is the original node value and value is the cloned node.


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None

        old_to_new = {}
        seen = set()
        q = deque([node])
        seen.add(node.val)
        while q:
            curr = q.popleft()
            curr_cp = old_to_new.setdefault(curr.val, Node(curr.val))

            for neighbor in curr.neighbors:
                neighbor_cp = old_to_new.setdefault(neighbor.val, Node(neighbor.val))
                curr_cp.neighbors.append(neighbor_cp)

                if neighbor.val not in seen:
                    q.append(neighbor)
                    seen.add(neighbor.val)

        return old_to_new[1]

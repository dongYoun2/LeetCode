# problem: https://leetcode.com/problems/clone-graph/
# submission: https://leetcode.com/problems/clone-graph/submissions/1231246199/

# 30 min
# runtime: 35 ms, memory: 18.2 MB
# TC: O(V + E), where V is the number of nodes and E is the number of edges
# SC: O(2V) -> O(V) (for the visited dict and the queue)

# From LeetCode Top Interview 150 - Graph General

# This is my third time solving this problem. I solved it on 04/13/2024 and 12/04/2024.

# I used BFS to solve this problem. The key idea is to store the cloned nodes in a hash table (`visited`), which also serves as a visited set. At first, I simply used a set to store them, but I realized that I needed to access the cloned nodes later, which could be done by using a dictionary key.

# cf.) This problem can also be solved using DFS or simply the Python deepcopy module although the latter is not intended.


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

        visited = {node.val: Node(node.val)}
        q = deque([node])
        while q:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    q.append(neighbor)

                cloned_neighbor = visited.setdefault(neighbor.val, Node(neighbor.val))
                visited[curr.val].neighbors.append(cloned_neighbor)

        return visited[1]


# notes while solving:
# 1: 2, 4
# 2: 1, 3
# 3: 2, 4
# 4: 1, 3

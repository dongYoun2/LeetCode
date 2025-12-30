# submission: https://leetcode.com/problems/clone-graph/submissions/1805137208/
# runtime: 41 ms, memory: 18.4 MB

# 46 min
# TC: O(V + E), where V is the number of nodes and E is the number of edges
# SC: O(V) (for the queue and the visited set. also, the cloned graph is not counted since it's an output space.)


# took much longer than expected. the code below is a little verbose and inefficient as it uses multiple traversals of the graph.

# KEY TAKEAWAY: the whole point of using visited or seen set when using queue (or BFS) is to avoid "reinserting" the same node into the queue. therefore, we need to check if the node is in the visited set before enqueuing it and add it to the visited set after enqueuing it. i was a little confused when to add; whether after dequeuing it or after enqueuing it.

# cf.) refer to the 05_12_2025.py for the efficient and concise solution. the core logic is pretty much the same, but the implementation is a little different.


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
        if not node: return None

        q = deque([node])
        visited = {node.val, }

        graph = dict()
        while q:
            curr = q.popleft()
            if curr.val not in graph:
                graph[curr.val] = curr

            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    q.append(neighbor)
                    visited.add(neighbor.val)


        cp_graph = dict()
        for i, node in graph.items():
            cp_graph[i] = Node(node.val)

        for i, node in graph.items():
            for neighbor in node.neighbors:
                cp_graph[i].neighbors.append(cp_graph[neighbor.val])

        return cp_graph[1]

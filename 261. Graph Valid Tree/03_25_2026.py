# submission: https://leetcode.com/problems/graph-valid-tree/submissions/1958842332/
# runtime: 64 ms (beats  5.57%), memory: 20.32 MB (beats 81.64%)
# 35 min

# TC: O(V + E), where V is the number of vertices and E is the number of edges.
# SC: O(V + E)


# took longer than expected. though topological sorting with BFS is usually used on a directed graph, i can employ this idea here with an undirected graph; which would be so called as leaf peeling (or leaf trimming) algorithm. but there are several things to consider. first, in a process of peeling the leaves, the corresponding neighbor could also be a leaf node. we need to handle this case using the `if graph[v]` condition ass shown in the code below. moreover, another thing to be aware of is that without the edge count trick (`len(edges) == n - 1`), this algorithm may fail on a disconnected graph as you can see here: https://leetcode.com/problems/graph-valid-tree/submissions/1958898183/.

# more typical solutions for this problem would be:
# 1. cycle detection using DFS or BFS (needs parent tracking), or
# 2. edge count trick + graph connectivity detection using DFS, BFS (X need parent tracking since we use early return with an edge count trick), or Union-Find

# cf.) one funny thing is that i was planning to use BFS with queue data structure (i imported deque in the beginning), but i forgot, and ended up implementing the algorithm without it lol. with queue, the runtime becomes much faster as you can see in this submission: https://leetcode.com/problems/graph-valid-tree/submissions/1958849940/.


from collections import deque, defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        while True:
            leaf_nodes = [v for v, nghbrs in graph.items() if len(nghbrs) == 1]
            if not leaf_nodes:
                break

            for v in leaf_nodes:
                if graph[v]:    # avoids popping from empty set
                    nghbr = graph[v].pop()
                    graph[nghbr].remove(v)
                
        return all(len(graph[v]) == 0 for v in graph)

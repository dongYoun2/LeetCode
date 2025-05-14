# problem: https://leetcode.com/problems/evaluate-division/
# submission: https://leetcode.com/problems/evaluate-division/submissions/1633414777/

# 60 min
# TC: O(V+E) + O(Q*(V+E)) -> O(Q*(V+E)), where V, E, Q are the number of vertices, edges and queries respectively (cosntructing graph: O(V+E), DFS: O(V+E))
# SC: O(V + E + 2*V) -> O(V+E) (constructing graph: O(V+E), visited set: O(V), stack: O(V), and output space is not counted)

# From LeetCode Top Interview 150 - Graph General


# Since I selected this problem from LeetCode Top Interview 150 - Graph General, I knew that it was a graph problem. (If I didn't know, it would have taken a while to realize that it is a graph problem.) However, it still took quite a long time to solve since I was trying to overengineer. Since we are processing multiple queries, doing an entire DFS for each and every query is inefficient. So, I tried to precompute a direct path weight (score) while constructing the graph, which would allow me to answer each query in O(1) time. However, the implementation was getting complicated. Also, a more important fact is that the time complexity for building a graph this way is O(V^2), which is inadequate when there are many vertices.

# Thus, I decided to construct the graph as is and do a DFS for each query. This is acceptable since the number of equations (edges) and queries (paths to explore) is only up to 20 (very small). One way to optimize this is the memoization technique to cache the DFS results for later queries. Moreover, I first tried to implement DFS using recursion, but I found out that iterative DFS is easier to implement in this case since we need to keep track of the path score and the DFS function is called multiple times (need to make sure everything is reinitialized).

# cf.) The best optimized solution for the case where many equations and queries exist is to use the Union-Find algorithm. For more details, refer to the Editorial section.


from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def construct_graph():
            graph = defaultdict(dict)

            for (v1, v2), w in zip(equations, values):
                graph[v1][v2] = w
                graph[v2][v1] = 1 / w

            return graph


        def dfs(graph, start_v, end_v):
            assert start_v != end_v

            stack = deque([(start_v, 1)])   # (vertex, path_score)
            visited = set([start_v])

            while stack:
                vertex, score = stack.pop()

                if vertex == end_v:
                    return score

                for neighbor, weight in graph[vertex].items():
                    if neighbor not in visited:
                        stack.append((neighbor, score * weight))
                        visited.add(neighbor)

            return -1


        vertices = set(v for eq in equations for v in eq)
        graph = construct_graph()

        ans = []
        for start_v, end_v in queries:
            # consider only valid vertices
            if start_v not in vertices or end_v not in vertices:
                ans.append(-1.0)
                continue
            # self-loop
            if start_v == end_v:
                ans.append(1.0)
                continue

            path_score = dfs(graph, start_v, end_v)
            ans.append(path_score)

        return ans


# notes while solving:
# a: b
# b: a, c
# c: b
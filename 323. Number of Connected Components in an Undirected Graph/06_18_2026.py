# submission: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/submissions/2037872985/
# runtime: 0 ms (beats 100.00%), memory: 20.22 MB (beats 91.79%)
# 11 min
# solved with DFS

# TC: O(V + E), where V is the number of vertices and E is the number of edges
# SC: O(V)


# this is a typical dfs or bfs problem. i chose dfs with a stack implementation (i usually prefer recursive approach, but this time, i just tried iterative approach with stack data structure).

# cf.) this problem can also be solved with a union-find approach. 


from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def build_graph():
            g = defaultdict(list)
            for v1, v2 in edges:
                g[v1].append(v2)
                g[v2].append(v1)
            
            return g
        

        def dfs(node):
            nonlocal visited
            stack = deque([node])
            visited.add(node)

            while stack:
                curr = stack.pop()

                for nghbr in graph[curr]:
                    if nghbr not in visited:
                        stack.append(nghbr)
                        visited.add(nghbr)


        ans = 0
        visited = set()
        graph = build_graph()
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                ans += 1

        return ans

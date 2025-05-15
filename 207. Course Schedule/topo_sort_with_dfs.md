[Problem]()

## Cycle Detection Using Topologcial Sort with DFS


- [Submission](https://leetcode.com/problems/course-schedule/submissions/1634338367/)
- Runtime: 7 ms, Memory: 21.2 MB
- TC: $O(V + E)$, where V (vertices) is the number of courses and E (edges) is the number of prerequisites.
- SC: $O(V + E)$ (`graph`: $O(V+E)$, `visited` list and `instack` set: $O(V)$, recursion stack: $O(V)$)
<br>

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def construct_graph():
            graph = {i: set() for i in range(numCourses)}
            for c, pre in prerequisites:
                graph[pre].add(c)
            return graph

        def has_cycle_dfs(node, visited, instack):
            if node in instack:
                return True

            if visited[node]:
                return False

            instack.add(node)

            for nghbr in graph[node]:
                if has_cycle_dfs(nghbr, visited, instack):
                    return True

            instack.remove(node)    # backtrack

            # mark as done, record post-order
            visited[node] = True
            # topo_list.append(node)

            return False

        graph = construct_graph()

        visited = [False] * numCourses
        instack = set() # current DFS path
        # topo_list = []  # will first hold reversed topo sorted list

        for node in range(numCourses):
            if not visited[node]:
                if has_cycle_dfs(node, visited, instack):
                    return False

        # topo_list.reverse()
        return True

```
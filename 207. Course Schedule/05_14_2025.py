# submission: https://leetcode.com/problems/course-schedule/submissions/1634293646/
# runtime: 3 ms, memory: 19.6 MB

# 20 min
# TC: O(V + E), where V (vertices) is the number of courses and E (edges) is the number of prerequisites.
# SC: O(V + E) (graph: O(V+E), indegree: O(V), queue and topo_list: O(V))

# From LeetCode Top Interview 150 - Graph General

# This is my fourth attempt at this problem. I solved it on 04/15/2024, failed on 12/07/2024, and again solved it on 02/21/2025. I now fully understand this problem and the topological sorting algorithm.

# The problem concerns detecting cycles in a directed graph. This cycle detection can be done by topological sorting. The below solution uses BFS to perform topological sorting, which is also known as Kahn's algorithm. The core idea of this algorithm is to maintain a list of vertices with no incoming edges (indegree = 0) and iteratively remove them from the graph while updating the in-degree of their neighbors. If we can remove all the vertices, it means there are no cycles in the graph.

# DFS can also be used for topological sorting. For more details, refer to the markdown file or the Editorial section.

# cf.) Removing `del indegree[vertex]` line also works in this code since we are inserting a neighbor with indegree 0 into the queue right after we decrease the indegree while iterating over the neighbors. Also, removing this line is okay here because we are not using the indegree dict anymore after the while loop.



from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def construct_graph():
            graph = {i: set() for i in range(numCourses)}
            indegree = {i: 0 for i in range(numCourses)}

            for curr, prev in prerequisites:
                graph[prev].add(curr)
                indegree[curr] += 1

            return graph, indegree

        graph, indegree = construct_graph()

        # topological sorting
        topo_list = []
        q = deque([i for i, deg in indegree.items() if deg == 0])

        while q:
            for _ in range(len(q)):
                vertex = q.popleft()
                topo_list.append(vertex)

                for neighbor in graph[vertex]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        q.append(neighbor)

                del indegree[vertex]


        return len(topo_list) == numCourses

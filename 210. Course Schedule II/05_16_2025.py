# problem: https://leetcode.com/problems/course-schedule-ii/
# submission: https://leetcode.com/problems/course-schedule-ii/submissions/1635246682/

# 19 min
# TC: O(V+E), where V (vertices) is the number of courses and E (edges) is the number of prerequisites.
# SC: O(V+E) (graph: O(V+E), visited and processing set: O(V), recursion stack: O(V))

# From LeetCode Top Interview 150 - Graph General

# Yesterday, I solved the "207. Course Schedule" problem using Kahn's algorithm (BFS) for cycle detection. Then, I also studied the DFS approach for cycle detection (or topological sorting), which I summarized in the "topo_sort_with_dfs.md" file. This problem is almost the same as the 207 problem, except that it requires returning the actual topological order of the courses. Although the BFS solution is more straightforward and direct, I implemented this problem using DFS since it's good to practice and recap the content I learned yesterday.


from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def construct_graph():
            graph = defaultdict(list)

            for curr, pre in prerequisites:
                graph[pre].append(curr)

            return graph


        def detect_cycle_dfs(node):
            if node in visited:
                return False

            if node in processing:
                return True

            processing.add(node)

            for neighbor in graph[node]:
                if detect_cycle_dfs(neighbor):
                    return True

            processing.remove(node)
            visited.add(node)
            topo_list.append(node)

            return False


        graph = construct_graph()
        topo_list = []
        visited = set()
        processing = set()
        for vertex in range(numCourses):
            if detect_cycle_dfs(vertex):
                return []

        topo_list.reverse()

        return topo_list

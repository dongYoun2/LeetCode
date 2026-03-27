# submission: https://leetcode.com/problems/course-schedule-ii/submissions/1635246682/
# runtime: 0 ms (beats 100%), memory: 19.88 MB (beats 99.98%)
# 19 min

# TC: O(V+E), where V (vertices) is the number of courses and E (edges) is the number of prerequisites.
# SC: O(V+E) (graph: O(V+E), visited and processing set: O(V), recursion stack: O(V))


# From LeetCode Top Interview 150 - Graph General

# Yesterday, I solved the "207. Course Schedule" problem using Kahn's algorithm (BFS) for cycle detection. Then, I also studied the DFS approach for cycle detection (or topological sorting), which I summarized in the "topo_sort_with_dfs.md" file. This problem is almost the same as the 207 problem, except that it requires returning the actual topological order of the courses. Although the BFS solution is more straightforward and direct, I implemented this problem using DFS since it's good to practice and recap the content I learned yesterday.

# 03/27/2026 add on: in `detect_cycle_dfs` function, we first check if a node is visited then check if it is in the processing set (current dfs path). However, it's usually safer and better to check vice versa because it clearly matches the real priority where cycle detection is the critical condition. moreover, this is the standard pattern everywhere, including dfs cycle detection, and topological sorting. though in the code below, the order doesn't matter (invariant) due to that we always remove the current node from the `processing` set right before we add it to the `visited` set. in words, a node is in either `processing` or `visited` never both. but still, it's better to foloow the standard pattern!


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

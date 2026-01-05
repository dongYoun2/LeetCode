# submission: https://leetcode.com/problems/course-schedule/submissions/1875745962/
# runtime: 2 ms, memory: 18.34 MB

# 17 min
# refer to the 05_14_2025.py for the complexity analysis.


# this is a typical topological sort problem.

# here, we can notice this is a cycle detection problem, equivalent to topological sorting in this case. since we are not required to return the exact cycle path if it exists, we can simply use Kahn's algorithm (BFS). DFS can also be used here, but BFS is more straightforward and easier to implement.

# cf.) for DFS approach, refer to the "topo_sort_with_dfs.md" file.


from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = {i: 0 for i in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        topo_list = []
        q = deque([c for c, deg in in_degree.items() if deg == 0])
        while q:
            for _ in range(len(q)):
                course = q.popleft()
                topo_list.append(course)
                for nxt_course in graph[course]:
                    in_degree[nxt_course] -= 1
                    if in_degree[nxt_course] == 0:
                        q.append(nxt_course)
        
        return len(topo_list) == numCourses

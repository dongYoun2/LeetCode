# submission: https://leetcode.com/problems/course-schedule-ii/submissions/1961004880/
# runtime: 7 ms (beats 28.99%), memory: 20.51 MB (beats 52.80%)
# 14 min

# TC: O(V + E)
# SC: O(V + E)


# this problem is a typical topological sorting problem. Kahn's algorithm with BFS (leaf peeling) is the most straightforward to implement.


from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = {v: 0 for v in range(numCourses)}
        graph = defaultdict(set)

        for nxt, prev in prerequisites:
            in_degree[nxt] += 1
            graph[prev].add(nxt)

        ans = []
        q = deque([v for v in in_degree if in_degree[v] == 0])
        
        while q:
            v = q.popleft()
            ans.append(v)

            for nghbr in graph[v]:
                in_degree[nghbr] -= 1
                if in_degree[nghbr] == 0:
                    q.append(nghbr)
            
            del graph[v]
        
        return ans if len(ans) == numCourses else []

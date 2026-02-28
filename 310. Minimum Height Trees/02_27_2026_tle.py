# submission: https://leetcode.com/problems/minimum-height-trees/submissions/1933089430/
# time limit exceeded
# 29 min


# TC: O(n^2), where n is the number of vertices in the graph.
# SC: O(n)

# looking at the constraints that n can be as large as 20K, i knew that i needed to solve less than O(n log n) time. however, i couldn't think of a better appraoch so i first implemented the brute force solution as shown below. the time complexity is O(n^2) since for each vertex, i need to traverse all other vertices.

# what this approach does is that it calculates the height of the tree for each vertex, and then returns the vertex with the minimum height. the height of the tree is calculated by traversing the tree level by level.

# cf.) this problem can be solved with two different approaches: 1) BFS leaf-trimming approach (topological sorting), and 2) the diameter approach, which finds the diameter of the tree by running BFS (or DFS) twice, and computes the center of the tree. i thought of topo sort as the problem seems to be somewhat related to addressing the degree of the vertices, but i wasn't able to concretize and apply it.


from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        h_to_roots = defaultdict(list)
        for v in g:
            q = deque([v])
            visited = {v}
            height = -1

            while q:
                for _ in range(len(q)):
                    curr_v = q.popleft()
                    for nghbr in g[curr_v]:
                        if nghbr not in visited:
                            q.append(nghbr)
                            visited.add(nghbr)
                    
                height += 1
            
            h_to_roots[height].append(v)
        
        if not h_to_roots:
            return [0]

        min_h = min(h_to_roots)
        return h_to_roots[min_h]
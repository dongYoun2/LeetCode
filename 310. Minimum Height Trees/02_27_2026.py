# submission: https://leetcode.com/problems/minimum-height-trees/submissions/1933115697/
# runtime: 76 ms (beats 17.27%), memory: 32.06 MB (beats 9.74%)
# 65 min (including 02_27_2026_tle.py time; once 50 min passed, i looked at the topic tags and the hint. then i was able to solve it in 15 min.)

# TC: O(n), where n is the number of vertices in the graph (or tree).
# SC: O(n)


# below is a BFS leaf-trimming approach, just like the topological sorting. for this problem, the most important fact is that "the root of a Minimum Height Tree must be the center of the tree's diameter." The diameter of a tree is the longest path between any two nodes. therefore, the number of MHT roots is either 1 or 2, depending on the parity of the number of vertices in a diameter (the leetcode hint was asking "at most how many MHT roots can there be?").

# if we peel the tree layber by layer from outside inwards, only the center vertices will remain eventually.



from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]

        g = defaultdict(set)
        deg = defaultdict(int)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

            deg[a] += 1
            deg[b] += 1

        q = deque()
        for v, d in deg.items():
            if d == 1:
                q.append(v)

        while q:
            if len(deg) <= 2:
                return list(deg.keys())

            for _ in range(len(q)):
                curr_v = q.popleft()

                assert len(g[curr_v]) == 1
                nghbr = g[curr_v].pop()
                del g[curr_v]
                g[nghbr].remove(curr_v)

                del deg[curr_v]
                deg[nghbr] -= 1

                if deg[nghbr] == 1:
                    q.append(nghbr)

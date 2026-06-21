# submission: https://leetcode.com/problems/minimum-knight-moves/submissions/2039774486/
# runtime: 2978 ms (beats 48.27%), memory: 81.20 MB (beats 32.74%)
# 12 min
# solved using bfs

# TC: O(V+E) -> O(V + 8V) (since E <= 8V) -> O(V) -> O(d^2), where d is the shortest distance from the origin to the target. (BFS explores roughly all cells reachable within d moves)
# SC: O(V) -> O(d^2)


# this problm can be solved using bfs. here, the vertices are the board cells, and the edges are the possible knight moves. since there are 8 possible moves, we know that each cell has at most 8 neighbors. then, the shortest path is the minimum moves to reach the target cell from the origin.

# we can also optimize the algorithm considering the symmetry of the board (e.g. (x, y), (-x, y), (x, -y), (-x, -y) are equivalent.):
# 1. convert the target coordinates to the first quadrant.
# 2. limit the search space allowing coordinates down to -2 (x >= -2 and y >= -2) since sometimes the shortest path temporarily goes negative. (e.g. target: (1, 1), shortest path: (0, 0) -> (2, -1) -> (1, 1))

# the code for the optimized version can be found below: 
# https://leetcode.com/problems/minimum-knight-moves/submissions/2040370518/
# runtime: 727 ms (beats 63.96%), memory: 31.42 MB (beats 66.82%)


from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        q = deque([(0, 0)])
        visited = {(0, 0),}
        ans = 0

        while q:
            for _ in range(len(q)):
                cx, cy = q.popleft()

                if cx == x and cy == y:
                    return ans
                
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy

                    if (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
                
            ans += 1

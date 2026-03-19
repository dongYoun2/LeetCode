# submission: https://leetcode.com/problems/shortest-path-to-get-food/submissions/1953289485/
# runtime: 67 ms (beats 56.96%), memory: 28.63 MB (beats 47.09%)
# 19 min


# this is a typical BFS problem. it's pretty straightforward to notice that we need to use BFS.


from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        sy, sx = tuple((i, j) for i in range(m) for j in range(n) if grid[i][j] == '*')[0]

        q = deque([(sy, sx)])
        visited = {(sy, sx)}
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        ans = 1
        while q:
            for _ in range(len(q)):
                y, x = q.popleft()

                for dy, dx in dirs:
                    ny, nx = y + dy, x + dx

                    if not (0 <= ny < m and 0 <= nx < n):
                        continue
                    
                    if grid[ny][nx] == '#':
                        return ans

                    if (ny, nx) not in visited and grid[ny][nx] != 'X':
                        q.append((ny, nx))
                        visited.add((ny, nx))

            ans += 1

        return -1

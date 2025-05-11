# problem: https://leetcode.com/problems/number-of-islands/
# submission: https://leetcode.com/problems/number-of-islands/submissions/1631281570/

# 10 min
# runtime: 274 ms, memory: 20.6 MB
# TC: O(m * n), where m is the number of rows and n is the number of columns in the grid.
# SC: O(m * n)

# From LeetCode Top Interview 150 - Graph General

# This is the second time solving this problem. I have solved it on 02/20/2025.

# It's a classic graph-based problem, which can be solved using either DFS or BFS. I chose to solve it with recursive DFS.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        cnt = 0
        visited = [[False] * n for _ in range(m)]

        dys = [1, 0, -1, 0]
        dxs = [0, 1, 0, -1]
        is_valid = lambda r, c: 0 <= r < m and 0 <= c < n

        def dfs(y, x):
            visited[y][x] = True

            for dy, dx in zip(dys, dxs):
                next_y, next_x = y + dy, x + dx

                if is_valid(next_y, next_x) and not visited[next_y][next_x] and grid[next_y][next_x] == '1':
                    dfs(next_y, next_x)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1

        return cnt

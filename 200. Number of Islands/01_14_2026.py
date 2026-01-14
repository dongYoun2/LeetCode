# submission: https://leetcode.com/problems/number-of-islands/submissions/1885304512/
# runtime: 298 ms, memory: 30.9 MB

# 7 min
# refer to the "05_11_2025.py" for a complexity analysis.


# this is a typical graph problem, which could be easily solved using DFS or BFS. below code is a DFS solution.

# cf.) BFS solution can be found at: https://leetcode.com/problems/number-of-islands/submissions/1236293045/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(y, x):
            visited.add((y, x))

            dys = [-1, 0, 1, 0]
            dxs = [0, 1, 0, -1]
            
            is_valid = lambda r, c: 0 <= r < m and 0 <= c < n

            for dy, dx in zip(dys, dxs):
                n_y, n_x = y + dy, x + dx

                if is_valid(n_y, n_x) and grid[n_y][n_x] != '0' and (n_y, n_x) not in visited:
                    dfs(n_y, n_x)


        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '0' and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1
        
        return ans

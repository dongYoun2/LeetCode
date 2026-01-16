# submission: https://leetcode.com/problems/rotting-oranges/submissions/1887231357/
# runtime: 3 ms, memory: 19.56 MB

# 19 min
# refer to the README.md for the complexity analysis.


# this is a typical BFS problem. as soon as i saw the problem, i thought of using BFS.

# cf.) though the code is correct, we actually don't need to use the `visited` set since we can simply mark the cell as rotten. moreover, instead of using fixed orange counts, we can keep track of only the fresh oranges. this allow us to:
# 1. use `while q and fresh_cnt > 0` instead of `while q`
# 2. put `return` statement all at once.

# these are reflected in the README.md code.


from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = deque()
        visited = set()
        ans = fresh_cnt = rotten_cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                elif grid[i][j] == 2:
                    rotten_cnt += 1
                    q.append((i, j))
                    visited.add((i, j))

        if fresh_cnt == 0:
            return 0

        is_valid = lambda y, x: 0 <= y < m and 0 <= x < n
        dys = [1, 0, -1, 0]
        dxs = [0, 1, 0, -1]

        while q:
            for _ in range(len(q)):
                y, x = q.popleft()

                for dy, dx in zip(dys, dxs):
                    y_n, x_n = y + dy, x + dx

                    if is_valid(y_n, x_n) and grid[y_n][x_n] == 1 and (y_n, x_n) not in visited:
                        grid[y_n][x_n] = 2
                        q.append((y_n, x_n))
                        visited.add((y_n, x_n))
            
            ans += 1
            if len(visited) == fresh_cnt + rotten_cnt:
                return ans
        
        return -1

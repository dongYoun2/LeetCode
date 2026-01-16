[Problem](https://leetcode.com/problems/rotting-oranges/)

## BFS Approach

The logic is exactly the same as the `01_16_2025.py` solution, but removed unnecessary variables and made the code more concise.

- [Submission](https://leetcode.com/problems/rotting-oranges/submissions/1887235538/) (Runtime: 7 ms, Memory: 19.40 MB)
- TC: $O(m*n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid.
  - first double loop: $O(m*n)$
  - BFS: $O(m*n*4) -> O(m*n)$
- SC: $O(m*n)$


```python
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        ans = fresh_cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        is_valid = lambda r, c: 0 <= r < m and 0 <= c < n

        while q and fresh_cnt > 0:
            for _ in range(len(q)):
                y, x = q.popleft()
                
                for dy, dx in zip(dys, dxs):
                    y_n, x_n = y + dy, x + dx

                    if is_valid(y_n, x_n) and grid[y_n][x_n] == 1:
                        q.append((y_n, x_n))
                        grid[y_n][x_n] = 2
                        fresh_cnt -= 1

            ans += 1

        return ans if fresh_cnt == 0 else -1
```
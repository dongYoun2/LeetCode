[Problem](https://leetcode.com/problems/surrounded-regions/)


## DFS + Optimization Technique

Below is the optimized version of the **05_11_2025.py** solution. The simple optmization technique is only to start the DFS traversal from the cells that are on the border of the board and have the value 'O', instead of traversing the all cells with value 'O'.
<br>

- [Submission](https://leetcode.com/problems/surrounded-regions/submissions/1631390724/) (runtime: 19 ms, memory: 22.5 MB)
- TC: $O(mn)$, where $m$ is the number of rows and $n$ is the number of columns in the board. (Although the time complexity is the same as the the **05_11_2025.py** solution, it's much faster in practice.)
- SC: $O(mn)$ (`visited` array, `border_region_set` set, and recursion stack all require $O(mn)$ space.)

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        is_valid = lambda r, c: 0 <= r < m and 0 <= c < n
        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        def find_island(y, x):
            ret = {(y, x)}
            visited[y][x] = True

            for dy, dx in zip(dys, dxs):
                y_n, x_n = y + dy, x + dx

                if is_valid(y_n, x_n) and not visited[y_n][x_n] and board[y_n][x_n] == 'O':
                    partial = find_island(y_n, x_n)
                    ret.update(partial)

            return ret

        is_border = lambda r, c: r == 0 or r == m - 1 or c == 0 or c == n - 1
        border_region_set = set()

        for i in range(m):
            for j in range(n):
                if is_border(i, j) and board[i][j] == 'O':
                    border_region = find_island(i, j)
                    border_region_set.update(border_region)

        for i in range(m):
            for j in range(n):
                if (i, j) not in border_region_set and board[i][j] == 'O':
                    board[i][j] = 'X'
```
<br>

Below is the Editorial Approach 1's solution with some modifications for better readability.
<br>

- [Submission](https://leetcode.com/problems/surrounded-regions/submissions/1631397854/) (runtime: 7 ms, memory: 21.9 MB)
- TC: $O(mn)$
- SC: $O(mn)$, but no `visited` array and `border_region_set` set are needed since we are modifying the board in place. (only for the recursion stack space)

```python
from itertools import product

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        is_valid = lambda r, c: 0 <= r < m and 0 <= c < n

        def dfs(y, x):
            if board[y][x] != "O":
                return

            board[y][x] = "E"
            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx
                if is_valid(ny, nx):
                    dfs(ny, nx)

        borders = list(product(range(m), [0, n - 1])) + list(product([0, m - 1], range(n)))

        # mark the "escaped" cells, with any placeholder, e.g. 'E'
        for r, c in borders:
            dfs(r, c)

        # flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"  # captured
                elif board[i][j] == "E":
                    board[i][j] = "O"  # escaped
```
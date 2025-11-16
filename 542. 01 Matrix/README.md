[Problem](https://leetcode.com/problems/01-matrix/)

## DP Approach

Refer to the `11_16_2025.py` solution.


## BFS Approach


Naive BFS approach would be performing BFS for each and every cell. However, the time complexity would be $O(m^2 \cdot n^2)$, which is very inefficient.

However, we can view this problem simlar to the topological sorting. The 0 cells are the source vertices, where no incoming edges exist. We can simply perform BFS from all the 0 cells and update the distance of the 1 cells. To do this, we first need to enqueue all the 0 cells and mark them as visited, and keep adding one to the each level of the BFS traversal if the cell is not visited yet.


- [Submission](https://leetcode.com/problems/01-matrix/submissions/1831006319/) (Runtime: 138 ms, Memory: 20.42 MB)
- TC: $O(m \cdot n)$
- SC: $O(m \cdot n)$ (for queue and the `visited` array)


```python
from collections import deque
import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        visited = [[False] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = True

        # BFS
        dys = [1, -1, 0, 0]
        dxs = [0, 0, -1, 1]

        while q:
            y, x = q.popleft()

            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx
                if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:
                    mat[ny][nx] = mat[y][x] + 1

                    q.append((ny, nx))
                    visited[ny][nx] = True

        return mat

```
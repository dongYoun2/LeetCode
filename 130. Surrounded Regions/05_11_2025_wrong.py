# problem: https://leetcode.com/problems/surrounded-regions/
# submission: https://leetcode.com/problems/surrounded-regions/submissions/1631324246/

# This is a wrong solution, which I tried to solve with a backtracking approach.


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        is_valid = lambda r, c: 0 <= r < m and 0 <= c < n
        is_boarder = lambda r, c: r == 0 or r == m - 1 or c == 0 or c == n - 1
        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        def capture_dfs(y, x):
            assert is_valid(y, x)
            visited[y][x] = True

            if is_boarder(y, x):
                return False

            ret = True
            for dy, dx in zip(dys, dxs):
                next_y, next_x = y + dy, x + dx

                if is_valid(next_y, next_x) and not visited[next_y][next_x] and board[next_y][next_x] == 'O':
                    board[next_y][next_x] = 'X'
                    if not capture_dfs(next_y, next_x):
                        ret = False
                        board[next_y][next_x] = 'O'

            return ret


        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                    if not capture_dfs(i, j):
                        board[i][j] = 'O'


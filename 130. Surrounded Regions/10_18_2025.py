# submission: https://leetcode.com/problems/surrounded-regions/submissions/1804722387/
# runtime: 4 ms, memory: 21.98 MB

# 39 min
# TC: O(m * n), where m and n are the number of rows and columns in the board, respectively
# SC: O(m * n), for the visited set and the recursion stack


# this is my second time solving this problem. at first, i tried to find all the regions (either surrounded or not). however, while debugging this approach, i realized that i can simply traverse only the boarder cells and find teh regions that are not surrounded, which has the boarder cells part of it. this is exactly the same approach as the solution on the markdown file.

# quite proud that i have solved it with a most optimal solution within 40 minutes.


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]
        is_valid = lambda r, c: 0 <= r < m and 0 <= c < n
        visited = set()


        def dfs(y, x):
            if not is_valid(y, x): return
            if (y, x) in visited: return
            if board[y][x] == 'X': return

            board[y][x] = 'NON_SURR_REGION_CELL'
            visited.add((y, x))

            for dy, dx in zip(dys, dxs):
                nxt_y, nxt_x = y + dy, x + dx
                dfs(nxt_y, nxt_x)


        for c in range(n):
            dfs(0, c)   # first row
            dfs(m - 1, c)   # last row

        for r in range(m):
            dfs(r, 0)   # first col
            dfs(r, n - 1)   # last col

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'NON_SURR_REGION_CELL':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

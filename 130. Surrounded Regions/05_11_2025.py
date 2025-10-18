# submission: https://leetcode.com/problems/surrounded-regions/submissions/1631371409/
# runtime: 2108 ms, memory: 46.4 MB

# 60 min
# TC: O(mn), where m is the number of rows and n is the number of columns
# SC: O(4mn) -> O(mn) (`visited`, `islands`, `region_index`, and the recursion stack)

# From LeetCode Top Interview 150 - Graph General

# In the beginning, I came up with the same idea as this code below. However, due to extra space complexity, I tried to do an in-place reflip for the regions that include border cells after the DFS traversal, which would be a backtracking solution ("05_11_2025_wrong.py"). Failing at the test case and debugging, I restarted from scratch and solved the problem with the code below.

# The algorithm is as follows:
# 1. DFS: Traverse the board and find all regions (or islands) (connected 'O's) using DFS.
# 2. Filter: For each region, filter out the regions connected to the border.
# 3. Flip: For each region that is not connected to the border, flip all 'O's to 'X's.

# The main problem with this code is that its execution time is too long in practice. It attempted to traverse all cells with 'O's, but this can be further optimized by starting a DFS traversal from the cells on the border that have 'O'. This optimized solution can be found in the markdown file.


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
            ret = [(y, x)]
            visited[y][x] = True

            for dy, dx in zip(dys, dxs):
                y_n, x_n = y + dy, x + dx

                if is_valid(y_n, x_n) and not visited[y_n][x_n] and board[y_n][x_n] == 'O':
                    partial = find_island(y_n, x_n)
                    ret.extend(partial)

            return ret

        islands = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    island = find_island(i, j)
                    islands.append(island)


        is_border = lambda r, c: r == 0 or r == m - 1 or c == 0 or c == n - 1

        # find which islands are not border islands
        region_index = [all(not is_border(r, c) for r, c in island) for island in islands]

        for i, island in enumerate(islands):
            if region_index[i]:
                for r, c in island:
                    board[r][c] = 'X'

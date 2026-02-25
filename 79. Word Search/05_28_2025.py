# submission: https://leetcode.com/problems/word-search/submissions/1647422137/
# runtime: 5064 ms (beats 16.52%), memory: 17.8 MB (beats 83.26%)
# 29 min

# TC: O(m*n*3^w), where m is the number of rows, n is the number of columns, and w is the length of the word.
# - We are exploring every possible path that starts from each cell.
# - There are 3 directions to move from each cell since we are not revisiting the cell we just came from.
# SC: O(w + m*n). O(w) for the recursion stack space and O(m*n) for the `in_path` tracking array.


# From LeetCode Top Interview 150 - Backtracking

# This is a DFS + backtracking problem. The solution itself is correct and the analyzed time complexity is also optimal. However, the execution time is long in practice. This can be optimized signficantly by early return with search pruning. For more details, refer to the markdown file.

# cf.) Other than search pruning, the solution can also be improved by slightly changing the logic of the `if` condition in the `dfs()` function's `for` loop. (Also described in the markdown file.)



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        is_valid = lambda y, x: 0 <= y < m and 0 <= x < n


        def dfs(y, x, curr_idx):
            if board[y][x] != word[curr_idx]:
                return False

            if curr_idx + 1 == len(word):
                return True

            in_path[y][x] = True

            ret = False
            for dy, dx in zip(dys, dxs):
                next_y, next_x = y + dy, x + dx
                if is_valid(next_y, next_x) and not in_path[next_y][next_x]:
                    ret = ret or dfs(next_y, next_x, curr_idx + 1)

            in_path[y][x] = False

            return ret


        in_path = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
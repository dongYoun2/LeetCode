# submission: https://leetcode.com/problems/word-search/submissions/1816209835/
# runtime: 5443 ms, memory: 18.14 MB

# 28 min
# the time and space complexity is the same as the 05_28_2025.py solution.


# the solution contains some duplicate code lines; for instance, backtracking and restoring logic exist in both the `dfs` for loop and the `dfs` function itself. the former is unnecessary actually. moreover, to make more readable code, we can simply check the very first character of the word in the main nested for loop, then call the `dfs` function if it matches. this helps to change the recursive function's termination condition from `pos + 1 >= len(word)` to `pos == len(word) - 1` (or >=). lastly, by applying three tricks, we can significantly optimize the runtime. for more details, refer to the markdown file.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]
        is_valid = lambda y, x: 0 <= y < m and 0 <= x < n


        def dfs(y, x, pos):
            if board[y][x] != word[pos]:
                return False

            # checking `pos + 1` (instead of `pos`) is needed at this place to address the board with only one element case
            if pos + 1 >= len(word):
                return True

            orig_temp = board[y][x]
            board[y][x] = '#'   # mark as visited

            for dy, dx in zip(dys, dxs):
                y_next, x_next = y + dy, x + dx

                if is_valid(y_next, x_next) and board[y_next][x_next] != '#':
                    temp = board[y_next][x_next]
                    if dfs(y_next, x_next, pos + 1):
                        return True

                    board[y_next][x_next] = temp

            board[y][x] = orig_temp
            return False


        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False

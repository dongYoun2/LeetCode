# problem: https://leetcode.com/problems/game-of-life/
# submission: https://leetcode.com/problems/game-of-life/submissions/1596585079/

# 13 min
# TC: O(8*m*n) -> O(m*n)
# SC: O(m*n) (board_cp)


from copy import deepcopy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        board_cp = deepcopy(board)

        dys = [-1, -1, 0, 1, 1, 1, 0, -1]
        dxs = [0, 1, 1, 1, 0, -1, -1, -1]

        is_valid = lambda y, x: 0 <= y < m and 0 <= x < n

        for y in range(m):
            for x in range(n):
                live_cnt = 0
                for dy, dx in zip(dys, dxs):
                    y_nxt, x_nxt = y + dy, x + dx

                    if is_valid(y_nxt, x_nxt) and board_cp[y_nxt][x_nxt] == 1:
                        live_cnt += 1

                if board_cp[y][x] == 1:
                    if live_cnt < 2 or live_cnt > 3:
                        board[y][x] = 0
                    else: # lives on next gen
                        board[y][x] = 1
                else:   # dead cell
                    if live_cnt == 3:
                        board[y][x] = 1

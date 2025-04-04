# problem: https://leetcode.com/problems/game-of-life/
# submission: https://leetcode.com/problems/game-of-life/submissions/1596789291/

# 25 min
# TC: O(2*8*m*n) -> O(m*n) (two-pass)
# SC: O(1) (in-place)

# Below solution uses constant space with O(m*n) time complexity.

# On the first pass, it counts the number of live neighbors and stores them on the board itself. One thing to notice is that the base number (base_cnt) is added to the count and then multiplied by the sign indicator (-1: was dead cell, +1: was live cell). This way, we can avoid a zero count of live neighbors (no sign) and also easily distinguish during the second pass whether the cell was originally alive or dead.

# In the second pass, we update the board as the output format based on the count of live neighbors and the cell's previous status (whether it was live or dead).

# This approach is slightly different from the LeetCode Editorial's solution for the follow-up question, where it uses a dummy cell value to signify the previous state of the cell along with the new changed value. The trick is to denote "live -> dead" as -1 and "dead -> live" as 2.


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        dys = [-1, -1, 0, 1, 1, 1, 0, -1]
        dxs = [0, 1, 1, 1, 0, -1, -1, -1]


        is_valid = lambda y, x: 0 <= y < m and 0 <= x < n
        base_cnt = 10   # can be any number greater than zero

        for y in range(m):
            for x in range(n):
                live_cnt = base_cnt # cannot be zero (any cell with no live neighbors gets 0 for temporary state, but all temp states should be either positive or negative)
                for dy, dx in zip(dys, dxs):
                    y_nxt, x_nxt = y + dy, x + dx

                    if is_valid(y_nxt, x_nxt) and board[y_nxt][x_nxt] > 0:  # to account already modified cell
                        live_cnt += 1

                sign = 1 if board[y][x] == 1 else -1    # +: was live, -: was dead
                board[y][x] = sign * live_cnt

        # second pass: update to next state
        for y in range(m):
            for x in range(n):
                if board[y][x] > 0: # live cell
                    live_cnt = board[y][x]
                    if live_cnt < base_cnt + 2 or live_cnt > base_cnt + 3:
                        board[y][x] = 0
                    else: # lives on next gen
                        board[y][x] = 1
                else:   # dead cell
                    live_cnt = - board[y][x]
                    if live_cnt == base_cnt + 3:
                        board[y][x] = 1
                    else:
                        board[y][x] = 0

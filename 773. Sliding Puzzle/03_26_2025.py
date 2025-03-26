# problem: https://leetcode.com/problems/sliding-puzzle/
# submission: https://leetcode.com/problems/sliding-puzzle/submissions/1587069028/

# 59 min
# TC: O((N*M)! * (N*M)), where N is the row count and M is the column count of the board (although the board is always 2x3, which is a constant, complexity is computed with N and M for generality)
# SC: O(N*M)

# I started with a DFS approach. However, I realized that the DFS approach was not efficient because DFS may visit the same node (state) multiple times, whereas BFS visits each node exactly once since it traverses the graph level by level. Even with the memoization technique, it doesn't guarantee that the first visit is the shortest path. In the question, a minimum number of moves is asked, which is just the shortest path. When finding the shortest path (or the length), BFS is usually the best choice.

from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        N, M = 2, 3
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    start_y, start_x = i, j
                    break

        answer_board = [[1,2,3],[4,5,0]]
        board_to_str = lambda board: "".join([str(e) for row in board for e in row])
        str_to_board = lambda board_s: [[int(board_s[M*i+j]) for j in range(M)] for i in range(N)]

        answer_str = board_to_str(answer_board)

        is_valid = lambda y, x: 0 <= y < N and 0 <= x < M
        visited = set()

        q = deque([(start_y, start_x, board_to_str(board))])
        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        move = 0
        while q:
            level_size = len(q)
            for _ in range(level_size):
                y, x, board_s = q.popleft()

                if board_s == answer_str:
                    return move

                visited.add(board_s)
                curr_board = str_to_board(board_s)

                for dy, dx in zip(dys, dxs):
                    y_n, x_n = y + dy, x + dx

                    if is_valid(y_n, x_n):
                        curr_board[y][x], curr_board[y_n][x_n] = curr_board[y_n][x_n], curr_board[y][x]
                        nxt_board_str = board_to_str(curr_board)
                        if nxt_board_str not in visited:
                            q.append((y_n, x_n, nxt_board_str))

                        curr_board[y][x], curr_board[y_n][x_n] = curr_board[y_n][x_n], curr_board[y][x] # restore the board

            move += 1

        return -1

# notes while solving the problem:
# 6! == 720
# problem: https://leetcode.com/problems/snakes-and-ladders/
# submission: https://leetcode.com/problems/snakes-and-ladders/submissions/1591231865/

# 59 min
# TC: O(n^2)
# SC: O(n^2)

# This is a typical BFS problem. Usually, graphs with the shortest path problems are solved with BFS.

# It took me a while to understand and solve the problem. Specifically, converting a board was a little confusing. At first, I thought all odd-indexed rows should be reversed, but it also depends on the parity of 'n'; thus, I had to check with ` n % 2 != i % 2`.

# This solution can be improved in two ways. Instead of converting to another 2D board, it could be converted to a 1D array (time complexity is the same as O(n^2)). Moreover, this problem can also be solved using the Dijkstra algorithm ((single-source shortest path) with priority queue (min-heap) (TC: O(n^2 log n)). For further details, consult the LeetCode Editorial section's BFS approach.


from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        converted_board = [[-1] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] != -1:
                    if n % 2 != i % 2:
                        converted_board[n-1-i][j] = board[i][j] - 1
                    else:
                        converted_board[n-1-i][n-1-j] = board[i][j] - 1

        to_2d_idx = lambda i: divmod(i, n)

        cnt = 0
        q = deque([0])
        visited = {0}

        while q:
            for _ in range(len(q)):
                idx = q.popleft()
                if idx == n**2 - 1:
                    return cnt

                for d in range(1, 7):
                    next_idx = min(idx + d, n**2 - 1)

                    y, x = to_2d_idx(next_idx)

                    if converted_board[y][x] != -1:
                        next_idx = converted_board[y][x]

                    if next_idx not in visited:
                        q.append(next_idx)
                        visited.add(next_idx)

            cnt +=1

        return -1


# notes while solving:
# (n-1, 0) -> 1
# (n-1, n-1) -> 1 + n
# (n-2, n-1) -> 1 + n + 1

# 15 -> (2, 2)

# (k - 1) // n
# (15 -1) divmod 6 -> (2, 2)

# 10 -> (1, 3)
# 12 -> (1, 5)

# 11 divmod 6  -> (1, 5)

# n 짝 row idx 홀
# n 홀 row idx 짝
## DFS with Memoization and Backtracking


Problem: [773. Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/)
<br>

#### Wrong code

This is the code that I wrote before transitioning to a BFS approach. I first attempted with a DFS. However, after realizing that the BFS could more effectively solve the problem while debugging the below code, I solved it with a BFS.

The below code has two problems:
1. Wrong `if` condition for the early return (DFS doesn't guarantee the shortest path for the first visit, so we have to not only check whether the node is visited but also compare the path length (move count) of the previous visit and the current visit)
2. Missing backtracking (forgot to restore the board)

```python
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

        answer_str = board_to_str(answer_board)

        is_valid = lambda y, x: 0 <= y < N and 0 <= x < M
        visited = {}

        def dfs(y, x, move):
            board_str = board_to_str(board)

            if board_str in visited:
                visited[board_str] = min(visited[board_str], move)
                return

            visited[board_str] = move

            dys = [-1, 0, 1, 0]
            dxs = [0, 1, 0, -1]

            for dy, dx in zip(dys, dxs):
                y_n, x_n = y + dy, x + dx
                if is_valid(y_n, x_n):
                    board[y][x], board[y_n][x_n] = board[y_n][x_n], board[y][x]
                    dfs(y_n, x_n, move + 1)


        dfs(start_y, start_x, 0)

        return visited.get(answer_str, -1)

```
<br>


#### Correct code

This problem could also be solved using DFS (although the optimal approach is a BFS). To solve it with a DFS, we have to use a **memoization** and **backtracking**. Memoization is used to cut down paths (branches) when we’ve already visited a node with a **smaller number of moves** than the current visit. Backtracking is also necessary to backtrack (restore) to the next previous available path after visiting the dead end branch.

- TC: $O((N*M)! * (N*M)^2)$ (for detailed explanation, see the LeetCode Editorial section.)
- SC: $O(N*M)$
- [submission result](https://leetcode.com/problems/sliding-puzzle/submissions/1587094221/)

```python
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

        answer_str = board_to_str(answer_board)

        is_valid = lambda y, x: 0 <= y < N and 0 <= x < M
        visited = {}

        def dfs(y, x, move):
            board_str = board_to_str(board)

            if board_str in visited and visited[board_str] <= move: # already visited, and that visit was the shortest path
                return

            visited[board_str] = move

            dys = [-1, 0, 1, 0]
            dxs = [0, 1, 0, -1]

            for dy, dx in zip(dys, dxs):
                y_n, x_n = y + dy, x + dx
                if is_valid(y_n, x_n):
                    board[y][x], board[y_n][x_n] = board[y_n][x_n], board[y][x]
                    dfs(y_n, x_n, move + 1)
                    board[y][x], board[y_n][x_n] = board[y_n][x_n], board[y][x] # backtracking: restore the board


        dfs(start_y, start_x, 0)

        return visited.get(answer_str, -1)

```
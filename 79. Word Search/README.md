[Problem](https://leetcode.com/problems/word-search/)

## Optmized DFS with Backtracking

Due to the **search pruning** technique, this solution is much more efficient than the  `05_28_2025.py`. There are two pruning techniques used:
1. **Length Check**: If the length of the word is greater than the total number of cells in the board, we can immediately return `False`. (However, due to the $m$, $n$, and $w$ conditions given in the problem statement, this technique doesn't provide much benefit in practice.)
2. **Character Count Check**: If any of the character count of the word exceeds that of the board, we can also return `False`. (Runtime becomes amlost 7x faster with this technique.)


A final slight improvement is the **early return** in the `dfs()` function's `for` loop: as soon as one neighbor finds the rest of the word, we immediately return `True` and stop searching. This avoids unnecessary exploration and efficiently bubbles up the success—since we only need to check for **existence**, not **count occurrences**. (Note the difference in code from the `05_28_2025.py` solution, where we continue searching all neighbors even after finding a match.)


- [Submission](https://leetcode.com/problems/word-search/submissions/1647429170/) (Runtime: 703 ms, Memory: 18.1 MB)
- TC: $O(m*n*3^w)$, where $m$ is the number of rows, $n$ is the number of columns, and $w$ is the length of the word. Note that the time complexity is the same as the `05_28_2025.py` solution.
- SC: $(w + m*n)$. Space complexity can be reduced to $O(w)$ by modifying the board in place to track path or set node's visited status, but I believe this is not the best practice.
<br>


```python
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        if len(word) > m * n:   # pruning 1
            return False

        board_cntr = Counter([e for row in board for e in row])
        word_cntr = Counter(word)

        if word_cntr - board_cntr:  # pruning 2
            return False

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        is_valid = lambda y, x: 0 <= y < m and 0 <= x < n


        def dfs(y, x, curr_idx):
            if board[y][x] != word[curr_idx]:
                return False

            curr_c = board[y][x]

            if curr_idx + 1 == len(word):
                return True

            in_path[y][x] = True

            for dy, dx in zip(dys, dxs):
                next_y, next_x = y + dy, x + dx
                if is_valid(next_y, next_x) and not in_path[next_y][next_x] and dfs(next_y, next_x, curr_idx + 1):
                    return True

            in_path[y][x] = False

            return False


        in_path = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False

```
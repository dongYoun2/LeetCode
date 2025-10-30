[Problem](https://leetcode.com/problems/word-search/)

## Optmized DFS with Backtracking

Due to the **search pruning** technique, this solution is much more efficient than the  `05_28_2025.py` and `10_30_2025.py`. There are two pruning techniques used:
In the code below, there are three tricks (two with search pruning and one with heuristic optimization):
1. **Length Check Pruning**: If the length of the word is greater than the total number of cells in the board, we can immediately return `False`. (However, due to the $m$, $n$, and $w$ conditions given in the problem statement, this technique doesn't provide much benefit in practice.)
2. **Character Count Check Pruning**: If any of the character count of the word exceeds that of the board, we can also return `False`. (Runtime becomes **5~7x faster** with this technique.)
3. **Search-ordering Heuristic**: We start from rarer end to prune faster. Specifically, we compare the count of the first and last character of the word and start from the rarer end. This is powerful in practice because it can significantly reduce the search space. For example, if we start from the common character, we will start thousands of DFS calls — most of which fail. (Just by applying this heuristic from the code applied with two pruning techniques above, the runtime **drops from around 1000 ms to 4 ms**!)


A final slight improvement is the **returning `True` directly** in the `dfs()` function's `for` loop if the rest of the word is found: as soon as one neighbor finds the rest of the word, we immediately return `True` and stop searching. This avoids unnecessary exploration and efficiently bubbles up the success—since we only need to check for **existence**, not **count occurrences**. (Note the difference in code from the `05_28_2025.py` solution, where we continue searching all neighbors even after finding a match.)


- [Submission](https://leetcode.com/problems/word-search/submissions/1816238765/) (Runtime: 4 ms, Memory: 18.08 MB)
- TC: $O(m*n*3^w)$, where $m$ is the number of rows, $n$ is the number of columns, and $w$ is the length of the word. Note that the time complexity is the same as the `05_28_2025.py` solution.
- SC: $(w + m*n)$. Space complexity can be reduced to $O(w)$ by modifying the board in place to track path or set node's visited status, but I believe this is not the best practice.


```python
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if m * n < len(word): return False  # first pruing

        w_counter = Counter(word)
        b_counter = Counter(c for row in board for c in row)
        if w_counter - b_counter: return False  # second pruning

        # Heuristic: start from rarer end to prune faster (third trick)
        if word.count(word[0]) > word.count(word[-1]):
            word = word[::-1]

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]
        is_valid = lambda y, x: 0 <= y < m and 0 <= x < n
        visited = set()


        def dfs(y, x, pos):
            if board[y][x] != word[pos]:
                return False
            if pos >= len(word) - 1:
                return True

            visited.add((y, x))
            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx
                if is_valid(ny, nx) and (ny, nx) not in visited:
                    if dfs(ny, nx, pos + 1):
                        return True

            visited.remove((y, x))
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False

```
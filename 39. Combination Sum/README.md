[Problem](https://leetcode.com/problems/combination-sum/)

## Backtracking (Recursive)

This approach is based on DFS with backtracking further optimized from `05_26_2025_backtracking_with_index.py` by pruning candidates that exceed the remaining target. To achieve this, we first sorted the candidates in ascending order.

- [Submission](https://leetcode.com/problems/combination-sum/submissions/1645534487/) (Runtime: 3 ms, Memory: 17.8 MB)
- TC: $O(n \log n + r \cdot d)$, where $n$ is the number of candidates, $r$ is number of returned combinations, and $d$ is max length of a combination ($d \approx $ `target` / `min(candidates)`).
- SC: $O(2d)$ -> $O(d)$. Recursion stack space and the combination storage space respectively. (output space is not counted)

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(curr, start, remain):
            if remain == 0:
                ans.append(curr[:])
                return

            for i in range(start, len(candidates)):
                # once a candidate exceeds remain, all further ones will too—break to prune
                if candidates[i] > remain: break

                curr.append(candidates[i])
                dfs(curr, i, remain - candidates[i])
                curr.pop()


        ans = []

        candidates.sort()   # sorting to prune larger values in one go
        dfs([], 0, target)

        return ans

```
<br>

## Backtracking (Iterative)

The exact same logic of backtracking (Recursive) appraoch is simply implemented with explicit stack management.

- [Submission](https://leetcode.com/problems/combination-sum/submissions/1645539231/) (Runtime: 6 ms, Memory: 17.8 MB)
- TC: $O(n \log n + B \cdot d)$, where $n$ is number of candidates, and $B$ is number of states explored. (This time complexity is more technically correct, but it won't hurt stating the time complexity same as the recursive version for simplicity.)
- SC: $O(B \cdot d)$. $B$ is the same as the above. It's the number of partial combs waiting to be explored. In the worst case, it's exponential in depth (same as the BFS queue burst). moreover, comb has the length up to $d$.

```python
from collections import deque

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        stack = deque([([], 0, target)])    # (current_comb, next_start_idx, remaining_sum)

        while stack:
            comb, start_idx, remain = stack.pop()

            if remain == 0:
                ans.append(comb)
                continue

            for i in range(start_idx, len(candidates)):
                c = candidates[i]

                # prune: once c > remain, all further ones will also be too big
                if c > remain: break

                # backtrack happens implicitly since original `comb` list is unchanged
                stack.append((comb + [c], i, remain - c))

        return ans

```
<br>


## BFS

This problem can also be solved with a BFS approach. In this case, in addition to values within the combination being in non-decreasing order, the combinations themselves will also be sorted in non-decreasing order by the number of elements in them.

- [Submission](https://leetcode.com/problems/combination-sum/submissions/1645546410/) (Runtime: 3 ms, Memory: 18 MB)
- TC: $O(n \log n + r \cdot d)$. (Symbols are the same as the above.)
- SC: $O(B \cdot d)$. In the worst case the queue can contain an entire breadth layer of partial combinations, which can be on the order of the total number of partial sequences of length up to $d$. So, it could be $O(n^d \cdot d)$ in the worst case.

```python
from collections import deque

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        q = deque([([], 0, target)])    # (current_combination, next_start_idx, remaining_sum)

        while q:
            comb, start_idx, remain = q.popleft()

            if remain == 0:
                ans.append(comb)
                continue

            for i in range(start_idx, len(candidates)):
                c = candidates[i]

                # prune: as soon as c > remain, no further candidates can fit
                if c > remain: break

                q.append((comb + [c], i, remain - c))

        return ans

```
<br>


## Dynamic Programming

- [Submission](https://leetcode.com/problems/combination-sum/submissions/1645549138/) (Runtime: 3 ms, Memory: 18 MB)
- TC: $O(nT + rd)$, where $n$ is the number of candidates, $T$ is the target, $r$ is the total number of combinations generated, and $d$ is the maximum length (depth) of a combination (approximately `target` / `min(candidates)`).
- SC: $O(T)$. For the `dp` array itself. (Output space is not counted.) (Note: storing the $r$ result lists costs $O(rd)$, but this is not counted since DP's own footprint is more important.) Additionally, in practice, we also store all partial combinations in `dp`, which can itself be exponential, similar to the output size.
<br>

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        candidates.sort()
        for cand in candidates:
            if cand > target: break

            for n in range(cand, target + 1):
                if n == cand:
                    dp[n].append([cand])
                else:
                    dp[n].extend([combs + [cand] for combs in dp[n-cand]])

        return dp[target]

```

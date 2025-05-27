[Problem](https://leetcode.com/problems/combination-sum/)

## Backtracking (Recursive)

This approach is based on DFS with backtracking further optimized from `05_26_2025_backtracking_with_index.py` by pruning candidates that exceed the remaining target. To achieve this, we first sorted the candidates in ascending order.

- [Submission](https://leetcode.com/problems/combination-sum/submissions/1645534487/) (Runtime: 3 ms, Memory: 17.8 MB)
- TC: $O(n \log n + n^d)$, where $n$ is the number of candidates and $d$ is the maximum depth of the recursion ($d \approx $ `target` / `min(candidates)`).
- SC: $O(2d)$ -> $O(d)$. Recursion stack space and the combination storage space respectively. (output space is not counted)
<br>

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
- TC: $O(n \log n + n^d)$. $O(n \log n)$ for sorting candidates.
- SC: $O((nd) \times d)$ -> $O(nd^2)$. Unlike the recursive version, the first $O(nd)$ presents because a fresh list is created for each candidate in the stack (`comb + [c]`) instead of explicit backtracking with `append()` and `pop()`. (This can be simply reduced with explicit backtracking.)
<br>

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
- TC: $O(n \log n + n^d)$. $O(n \log n)$ for sorting candidates.
- SC: $O(n^d \times d)$. In the worst case, queue can hold $O(n^d)$ partial combinations, each a list of length up to $d$.
<br>

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
- SC: $O(T)$. For the `dp` array itself. (Output space is not counted.) (Note: storing the $r$ result lists costs $O(rd)$, but this is not counted since DP's own footprint is more important.)
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

[Problem](https://leetcode.com/problems/combinations/)

## Fully Optimized Backtracking

- [Submission](https://leetcode.com/problems/combinations/submissions/1637027183/?envType=study-plan-v2&envId=top-interview-150) (Runtime: 95 ms, Memory: 59.7 MB)
- TC: $O(k \cdot \binom{n}{k}$ ($\binom{n}{k}$ means $n$ choose $k$)
- SC: $O(k)$. This is for the recursion stack, and the output space doesn't count.

The key to **backtracking** is to **prune the search space** as much as possible. In this case, we can avoid unnecessary recursive calls by **calculating the maximum starting number** for the next element in the combination based on how many elements are left to fill, as well as the early exit condition when the combination is complete.
<br>

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs_backtrack(last_num, comb):
            if len(comb) == k:
                ans.append(comb[:])
                return

            need_cnt = k - len(comb)
            max_start = n - need_cnt + 1

            for m in range(last_num + 1, max_start + 1):
                comb.append(m)
                dfs_backtrack(m, comb)
                comb.pop()  # backtrack


        ans = []
        dfs_backtrack(0, [])

        return ans
```
[Problem](https://leetcode.com/problems/combinations/)

## Fully Optimized Backtracking

- [Submission](https://leetcode.com/problems/combinations/submissions/1637027183/?envType=study-plan-v2&envId=top-interview-150) (Runtime: 95 ms, Memory: 59.7 MB)
- TC: $O(k \cdot \binom{n}{k}$ ($\binom{n}{k}$ means $n$ choose $k$)
- SC: $O(k)$. This is for the recursion stack, and the output space doesn't count.

The key to **backtracking** is to **prune the search space** as much as possible. In this case, we can avoid unnecessary recursive calls by two criteria:
1. **How many numbers are still needed** to complete a combination of length k.
2. **Whether there are enough remaining numbers** (from the current position up to n) to fill those remaining slots.

cf.) Note that `10_24_2025.py` solution only uses the second pruning criterion, and `05_18_2025_backtracking.py` doesn't prune anything, which is simply the pure backtracking approach.


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
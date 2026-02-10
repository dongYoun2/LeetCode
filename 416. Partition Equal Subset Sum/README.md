[Problem](https://leetcode.com/problems/partition-equal-subset-sum/)


Note that this problem is a variant of the [0/1 knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) ([백준 문제 링크](https://www.acmicpc.net/problem/12865)). Algorithmically, it's the same, and mathematically, partition is just the subset-sum decision version of 0/1 knapsack. The only difference is that 0/1 knapsack aims to maximize the value, whereas this problem aims to check if exact sum is achievable.

- `nums[i]` can be considered as a **weight** of the item.
- Here, weight and value are the same.
- Maximum capacity of the knapsack is half of the total sum of `nums`.

## DFS/Backtracking with Memoization (Top-down DP)

[Submission](https://leetcode.com/problems/partition-equal-subset-sum/submissions/1914061507/) — Runtime: 266 ms (Beats 89.63%), Memory: 83.02 MB (Beats 21.56%)

- TC: $O(n \cdot m)$, where $n$ is the length of the input list `nums`, and $m$ is the half of the total sum of `nums`.
- SC: $O(n \cdot m) + O(n)$ -> $O(n \cdot m)$
  - Memoization table: stores up to $n \cdot m$ states
  - Recursion stack: depth at most $n$


The code below is improved from the `02_04_2026_tle.py`. Instead of passing the chosen list `cands` to the recursive function as shown in the `02_04_2026_tle.py`, we use a single integer `remain` to define a proper **state** so that the `dfs` function can leverage the **memoization technique** utilized by the `lru_cache` decorator.

Moreover, note that we are using short-circuit evaluation to avoid unnecessary recursive calls in the `return` statement. If we keep variables (e.g. `take` and `skip`) to store the restuls, then doing `return take or skip` will lead to MLE. (submission: https://leetcode.com/problems/partition-equal-subset-sum/submissions/1914061106/)

```python
from functools import lru_cache
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        nums.sort(reverse=True)
        n = len(nums)

        # (optional) early exit: if the largest number already > target, impossible
        if nums[0] > target:
            return False


        @lru_cache(None)
        def dfs(i: int, remain: int) -> bool:
            # state: can we make 'remain' using nums[i:] ?
            if remain == 0:
                return True
            if i == n or remain < 0:
                return False

            return dfs(i + 1, remain - nums[i]) or dfs(i + 1, remain)


        return dfs(0, target)

```

## DP (Bottom-up) Approach

We can also solve with bottom-up dynamic programming approach. Here, `dp[i][s]` represents **whether we can make sum `s` using the first `i` numbers**; so we store the boolean value. Since the problem asks for whether exact sum is achievable, boolean value is enough.

However, in a classic knapsack problem, we store the integer value, where `dp[i][j]` indicates **the maximum achievable sum that is less than or equal to `j` using the first `i` numbers**. In other words, it asks for "What is the best sum I can build under capacity `j`?" (Note that we can also solve this problem in this way.)


For **complexity analysis**, let $n$ be the length of the input list `nums`, and $m$ be the half of the total sum of `nums`, which is `target = total // 2`.


### With 2D DP Table

[Submission](https://leetcode.com/problems/partition-equal-subset-sum/submissions/1914129394/) — Runtime: 1106 ms (Beats 38.79%), Memory: 35.08 MB (Beats 32.53%)

- TC: $O(n \cdot m)$
- SC: $O(n \cdot m)$

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: 
            return False
        target = total // 2
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            x = nums[i - 1]
            for s in range(target + 1):
                dp[i][s] = dp[i - 1][s]  # skip
                if s >= x:
                    dp[i][s] = dp[i][s] or dp[i - 1][s - x]  # take
            if dp[i][target]:
                return True

        return dp[n][target]

```

Solving with integer-value stored DP table (just like the classic knapsack problem), we can change some parts of the above code like this:

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # ... (same as above)

        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            x = nums[i - 1]
            for s in range(target + 1):
                if s < x:
                    dp[i][s] = dp[i - 1][s]   # skip only
                else:
                    dp[i][s] = max(
                        dp[i - 1][s],              # skip
                        dp[i - 1][s - x] + x       # take
                    )

            # early stop
            if dp[i][target] == target:
                return True

        return dp[n][target] == target
```


### With two 1D DP Tables (`prev` and `curr`)

[Submission](https://leetcode.com/problems/partition-equal-subset-sum/submissions/1914131662/) — Runtime: 458 ms (Beats 80.59%), Memory: 19.51 MB (Beats 58.27%)

- TC: $O(n \cdot m)$
- SC: $O(m)$


```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        prev = [False] * (target + 1)
        prev[0] = True

        for x in nums:
            curr = prev[:]  # start from skipping x
            for s in range(x, target + 1):
                curr[s] = curr[s] or prev[s - x]  # take x
            prev = curr
            if prev[target]:
                return True

        return prev[target]
```

### With one 1D DP Table (Backward Update)

[Submission](https://leetcode.com/problems/partition-equal-subset-sum/submissions/1914133070/) — Runtime: 443 ms (Beats 81.58%), Memory: 19.29 MB (Beats 77.98%)

- TC: $O(n \cdot m)$
- SC: $O(m)$

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums:
            # backward: dp[s-x] is from previous iteration (previous "row")
            for s in range(target, x - 1, -1):
                dp[s] = dp[s] or dp[s - x]
            if dp[target]:
                return True

        return dp[target]

```

### Bitset DP

[Submission](https://leetcode.com/problems/partition-equal-subset-sum/submissions/1914135218/) — Runtime: 0 ms (Beats 100.00%), Memory: 19.28 MB (Beats 77.98%)

- TC: $O(n \cdot m)$
- SC: $O(m)$ bits (packed into one integer)

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        bits = 1  # only sum 0 achievable
        for x in nums:
            bits |= bits << x  # add x to all existing sums

        return ((bits >> target) & 1) == 1

```
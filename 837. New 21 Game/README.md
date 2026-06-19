[Problem](https://leetcode.com/problems/new-21-game/)


## Dynamic Programming Approach

The key idea is to find the recurrent relation of the probability. Let `dp[x]` equals probability Alice reaches exactly `x` points. Alice only keeps drawing while **points < k**, so:

```
dp[x] = (dp[x-1] + dp[x-2] + ... + dp[x-maxPts]) / maxPts
```

More formally,

$$
dp[x] =
\frac{1}{maxPts}
\sum_{i=\max(0, x - maxPts)}^{x - 1}
\mathbf{1}_{i < k} \cdot dp[i]
$$

where

$$
\mathbf{1}_{i < k} =
\begin{cases}
1, & i < k \\
0, & i \ge k
\end{cases}
$$

Or, equivalently,

$$
dp[x] =
\frac{1}{maxPts}
\sum_{i=\max(0, x - maxPts)}^{\min(x - 1, k - 1)}
dp[i]
$$

The final answer is:

$$
\sum_{x=k}^{n} dp[x]
$$

Then, the question is **how can we compute the sum for each $x$ efficiently?**

[Naive DP](#naive-dp) recomputes this sum (`total`) for each $x$ (`score` in the code below) in $O(\text{maxPts})$ time, whereas [Sliding Window-optimized DP](#sliding-window-optimized-dp) computes this sum in $O(1)$ time by maintaining a window sum.

### Naive DP

[Submission](https://leetcode.com/problems/new-21-game/submissions/2039157902/)—Time Limit Exceeded

- TC: $O(n \cdot maxPts)$
- SC: $O(n)$

```python
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        for score in range(1, n + 1):
            total = 0.0

            for prev in range(max(0, score - maxPts), score):
                if prev < k:          # Alice can only draw from prev < k
                    total += dp[prev]

            dp[score] = total / maxPts
        
        # sum(dp[k:n+1])
        return sum(dp[k:])

```




### Sliding Window-optimized DP

We can optimize the naive DP solution by maintaining a window sum of the previous `maxPts` elements. 

The window size starts from 1 and increases by 1 until it reaches `maxPts`, but not all elements in the window are valid. More precisely, `window_sum` starts with `dp[0]`, and as points increases, it maintains the sum of valid previous states within the last maxPts points. A state is valid only if it is less than k, because Alice can only draw from scores < k.

[Submission](https://leetcode.com/problems/new-21-game/submissions/2039157800/)—Runtime: 27 ms (beats 44.61%), Memory: 19.79 MB (beats 39.78%)

- TC: $O(n)$
- SC: $O(n)$

```python
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        window_sum = 1.0
        ans = 0.0

        for points in range(1, n + 1):
            dp[points] = window_sum / maxPts

            if points < k:
                window_sum += dp[points]
            else:
                ans += dp[points]

            if points - maxPts >= 0:
                window_sum -= dp[points - maxPts]

        return ans

```
<br>

cf.) Instead of keeping the `ans` variable as a running sum, we can simply return the `sum(dp[k:])` just like the naive DP solution. The code is as follows:

[Submission](https://leetcode.com/problems/new-21-game/submissions/2039169075/)—Runtime: 27 ms (beats 44.61%), Memory: 19.68 MB (beats 79.18%)

```python
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        window_sum = 1.0

        for points in range(1, n + 1):
            dp[points] = window_sum / maxPts

            if points < k:
                window_sum += dp[points]

            if points - maxPts >= 0:
                window_sum -= dp[points - maxPts]

        return sum(dp[k:])

```

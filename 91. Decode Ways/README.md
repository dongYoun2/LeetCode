[Problem](https://leetcode.com/problems/decode-ways/)


## Dynamic Programming Solution

The pattern of this problem is the same as the [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) and **Fibonacci numbers** problems.

Once we define `dp[i]` as the number of ways to decode the substring `s[:i]`, the recurrent relation is:

```python
dp[i] =
    (dp[i - 1] if s[i - 1] is a valid 1-digit code else 0)
  + (dp[i - 2] if s[i - 2:i] is a valid 2-digit code else 0)
```

**Complexity Analysis**
- TC: $O(n)$
- SC: $O(n)$ (bottom-up: for the `dp` array; top-down: for the recursive stack)

### Bottom-up DP

[Submission](https://leetcode.com/problems/decode-ways/submissions/2059764956/)—Runtime: 3 ms (beats 26.24%), Memory: 19.22 MB (beats 69.93%)


- SC: $O(n)$ (for the `dp` array)


```python
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] = ways to decode s[:i]
        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):
            # Take one digit
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Take two digits
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

```
<br>

cf.) We can further optimize the above bottom-up DP solution to use constant space (i.e., SC: $O(1)$).


[Submission](https://leetcode.com/problems/decode-ways/submissions/2059765068/)—Runtime: 0 ms (beats 100.00%), Memory: 19.24 MB (beats 69.93%)

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        prev2 = 1  # dp[0]
        prev1 = 0 if s[0] == '0' else 1  # dp[1]

        for i in range(2, n + 1):
            curr = 0

            # Take one digit
            if s[i - 1] != '0':
                curr += prev1

            # Take two digits
            if 10 <= int(s[i - 2:i]) <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1

```
<br>


### Top-down DP (with Memoization)



[Submission](https://leetcode.com/problems/decode-ways/submissions/2059765685/)—Runtime: 0 ms (beats 100.00%), Memory: 19.84 MB (beats 7.38%)


```python
from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i: int) -> int:
            if i == 0:
                return 1

            ways = 0

            # Take one digit
            if s[i - 1] != '0':
                ways += dp(i - 1)

            # Take two digits
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                ways += dp(i - 2)

            return ways

        return dp(len(s))

```

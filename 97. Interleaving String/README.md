[Problem](https://leetcode.com/problems/interleaving-string/)


## Dynamic Programming


## Top-Down (with DFS) + Memoization

Start from `(i, j)` and recursively try taking the next character from either `s1` or `s2`. Cache each `(i, j)` result so the same state is never solved twice.


cf.) [04_01_2025.py](./04_01_2025.py) also follows this approach.


[Submission](https://leetcode.com/problems/interleaving-string/submissions/2116882746/)—Runtime: 47 ms (beats 79.54%), Memory: 20.05 MB (beats 29.75%)

- TC: $O(m*n)$, where $m$ and $n$ are the lengths of $s1$ and $s2$, respectively.
- SC: $O(n)$


```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        memo = {}

        def dfs(i, j):
            if i == m and j == n:
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            k = i + j

            if i < m and s1[i] == s3[k] and dfs(i + 1, j):
                return True

            if j < n and s2[j] == s3[k] and dfs(i, j + 1):
                return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0)

```


## Bottom-Up

### Using 2D DP Array

`dp[i][j]` means whether `s1[:i]` and `s2[:j]` can form `s3[:i+j]`. Build the table from smaller prefixes to larger prefixes.


cf.) [08_22_2026.py](./08_22_2026.py) also follows this approach.


[Submission](https://leetcode.com/problems/interleaving-string/submissions/2116890572/)—Runtime: 58 ms (beats 21.20%), Memory: 19.32 MB (beats 72.52%)

- TC: $O(m*n)$, where $m$ and $n$ are the lengths of $s1$ and $s2$, respectively.
- SC: $O(m*n)$


```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    continue

                from_s1 = i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

                dp[i][j] = from_s1 or from_s2

        return dp[m][n]

```


### Using 1D DP Array (Solves the Follow-Up Question)

Same idea as the 2D DP approach, but reuse one row because each state only depends on the current and previous row values. This reduces the space complexity from `O(m*n)` to `O(n)`.


[Submission](https://leetcode.com/problems/interleaving-string/submissions/2116893041/)—Runtime: 54 ms (beats 41.15%), Memory: 19.14 MB (beats 98.53%)

- TC: $O(m*n)$, where $m$ and $n$ are the lengths of $s1$ and $s2$, respectively.
- SC: $O(m*n)$


```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        dp = [False] * (n + 1)
        dp[0] = True

        # Use only s2
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # Use only s1
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                k = i + j - 1

                from_s1 = dp[j] and s1[i - 1] == s3[k]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[k]

                dp[j] = from_s1 or from_s2

        return dp[n]

```


[Problem](https://leetcode.com/problems/edit-distance/description/)

## Dynamic Programming

The problem of calculating the minimum edit distance between two strings can be solved using dynamic programming. The idea is to build a DP table where each cell `dp[i][j]` represents the minimum edit distance between the first `i` characters of `word1` and the first `j` characters of `word2`. (So, unlike `07_22_2025.py`, the DP table explicitly includes the empty string case.)

### Bottom-Up Approach

- [Submission](https://leetcode.com/problems/edit-distance/submissions/1707611880/) (Runtime: 67 ms, Memory: 21.2 MB)
- TC: $O(n \cdot m)$, where $n$ and $m$ are the lengths of `word1` and `word2`, respectively.
- SC: $O(n \cdot m)$ for the DP table.
<br>

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        # fill out the first row
        for j in range(1, m + 1):
            dp[0][j] = j

        # fill out the first column
        for i in range(1, n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return dp[-1][-1]

```



### Top-Down Approach: Recursive with Memoization

- [Submission](https://leetcode.com/problems/edit-distance/submissions/1707628706/) (Runtime: 31 ms, Memory: 19.7 MB)
- TC: $O(n \cdot m)$, where $n$ and $m$ are the lengths of `word1` and `word2`, respectively.
- SC: $O(2 n \cdot m)$ -> $O(n \cdot m)$ for the DP table and the recursion stack.
<br>


```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        # dp table for memoization; dp[r][c] = edit distance between
        # word1[:r] and word2[:c]
        dp = [[None] * (m + 1) for _ in range(n + 1)]

        def helper_min_dist(r: int, c: int) -> int:
            if r == 0:
                return c
            if c == 0:
                return r
            # return cached result
            if dp[r][c] is not None:
                return dp[r][c]

            if word1[r-1] == word2[c-1]:
                dp[r][c] = helper_min_dist(r - 1, c - 1)
            else:
                replace_op = helper_min_dist(r - 1, c - 1)
                delete_op = helper_min_dist(r - 1, c)
                insert_op = helper_min_dist(r, c - 1)
                dp[r][c] = min(replace_op, delete_op, insert_op) + 1

            return dp[r][c]

        return helper_min_dist(n, m)

```
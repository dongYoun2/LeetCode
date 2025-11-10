
## Expand From Centers (Two Pointers)

This approach is based on the **two-pointer algorithm**. The issue with the dynamic programming solution (`03_31_2025.py`) is that we always iterate over $\frac{n(n+1)}{2}$ times, leading to $O(n^2)$ time complexity. This is because we are focusing on the boundary of the substring — `(i, j)`, and there are $O(n^2)$ bounds. (In the DP solution, we maintain a 2D DP array, where dp[i][j] indicates whether the substring `s[i:j+1]` is palindrome or not.)

However, by changing our perspective to the center of the palindrome, we can get more advantages since there are $O(n)$ centers. With the two pointers `left` and `right`, we can move outward one by one from position `(i, i)` to check the odd-length palindrome, and from position `(i, i+1)` to check the even-length palindrome. Although the time complexity is the same as the DP solution, this approach is much **faster** in practice since most centers won't produce long palindromes.

- [Submission](https://leetcode.com/problems/longest-palindromic-substring/submissions/1826180866/) (Runtime: 282 ms, Memory: 17.78 MB)
- TC: $O(n^2)$, where $n$ is the length of the input string `s`
- SC: $O(1)$

Although the time complexity of this solution and the DP solution is the same, this approach is much faster in practice because of the following reasons:
1. **No table overhead**: Avoids the $O(n^2)$ DP table—no large memory allocation or repeated indexing.
2. **Early stopping**: Expansion around a center stops on first mismatch, so most centers do very little work.
3. **Better cache locality**: Reads the string contiguously near the center; DP’s scattered `dp[i+1][j-1]` accesses can cause more cache misses.

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s

        start, max_len = 0, 1  # best palindrome so far: s[start:start+max_len]

        def expand_around_center(l: int, r: int) -> None:
            nonlocal start, max_len
            while l >= 0 and r < n and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    start, max_len = l, curr_len
                l -= 1
                r += 1

        for i in range(n):
            # Odd-length palindrome (center at i)
            expand_around_center(i, i)
            # Even-length palindrome (center between i and i+1)
            expand_around_center(i, i + 1)

        return s[start:start+max_len]
```

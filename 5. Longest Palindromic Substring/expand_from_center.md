
## Expand From Centers

This approach is based on the **two-pointer algorithm**. The issue with the dynamic programming solution (`03_31_2025.py`) is that we always iterate over $\frac{n(n+1)}{2}$ times, leading to $O(n^2)$ time complexity. This is because we are focusing on the boundary of the substring — `(i, j)`, and there are $O(n^2)$ bounds. (In the DP solution, we maintain a 2D DP array, where dp[i][j] indicates whether the substring `s[i:j+1]` is palindrome or not.)

However, by changing our perspective to the center of the palindrome, we can get more advantages since there are $O(n)$ centers. With the two pointers `left` and `right`, we can move outward one by one from position `(i, i)` to check the odd-length palindrome, and from position `(i, i+1)` to check the even-length palindrome. Although the time complexity is the same as the DP solution, this approach is much **faster** in practice since most centers won't produce long palindromes.

Below code is from the LeetCode Editorial's Approach 3 code.

- TC: $O(n^2)$, where n is the length of the input string `s`
- SC: O(1)
- [Submission](https://leetcode.com/problems/longest-palindromic-substring/submissions/1592491546/) (submitted to compare the execution time with the DP code)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        ans = [0, 0]

        for i in range(len(s)):
            # (i, i): center of odd-length potential palindrome
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            # (i, i+1): center of even-length potential palindrome
            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans
        return s[i : j + 1]
```
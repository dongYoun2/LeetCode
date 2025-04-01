# problem: https://leetcode.com/problems/longest-palindromic-substring/
# submission: https://leetcode.com/problems/longest-palindromic-substring/submissions/1592488877/

# 15 min
# TC: O(n^2), where n is the length of the string
# SC: O(n^2)

# Since I knew that I had to use dynamic programming, finding the recurrent relation was not too difficult. I constructed a 2D dp array to implement the solution, and it felt very similar to the matrix chain multiplication problem, which is popular in 2D dynamic programming problems.

# In fact, there is further optimized solution (using two-pointer algorithm), where we can move outward from the center of the palindrome. For more details, refer to the markdown file or LeetCode Editorial section's "Approach 3: Expand From Centers".


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]

        # single letter substring is always palindrome
        ans = s[0]
        for i in range(len(s)):
            dp[i][i] = True

        # checking substring with two letters
        for i in range(1, len(s)):
            dp[i-1][i] = (s[i-1] == s[i])
            if dp[i-1][i]:
                ans = s[i-1:i+1]

        for diff in range(2, len(s)):
            for i in range(len(s) - diff):
                start, end = i, i + diff
                dp[start][end] = dp[start+1][end-1] and (s[start] == s[end])

                if dp[start][end]:
                    ans = s[start:end+1]

        return ans

# notes while solving:

# dp[i][j] (bool): s[i:j+1] is palindrome?
# s[i:j+1] is palindrome if s[i+1:j] is palindrome and s[i] == s[j]

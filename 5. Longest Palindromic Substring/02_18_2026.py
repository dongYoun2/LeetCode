# submission: https://leetcode.com/problems/longest-palindromic-substring/submissions/1923617381/
# runtime: 1922 ms (beats 23.20%), memory: 27.38 MB (beats 5.68%)
# 14 min

# refer to the 03_31_2025.py for a complexity analysis.


# solved with a 2D dp array (dynamic programming). DP cell comutation dynamics is similar to the matrix chain multiplication problem.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        assert s

        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = s[0]
        
        for i in range(n): # 1-char palinedrome
            dp[i][i] = True
        
        for i in range(n-1):    # 2-char palindrome
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = s[i:i+2]
        
        for d in range(2, n):
            for i in range(n-d):
                j = i + d
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    ans = s[i:j+1]
        
        return ans


# notes while solving:
# s[i][j] is a palindrome if s[i+1][j-1] is a palindrome and s[i] == s[j]

# submission: https://leetcode.com/problems/longest-palindromic-substring/submissions/1826136984/
# runtime: 2475 ms, memory: 25.46

# 20 min
# TC: O(n^2), where n is the length of the string
# SC: O(n^2) (2D dp array)


# didn't know which algorithm category this problem falls into, but noticed that it's a DP problem. just like the matrix chain multiplication problem, i solved it with a 2D dp array iterating from the diagonal to the top right corner.

# once i noticed that this is a DP problem, i also rememebered that this can be solved by finding the palindrome expanding from the center, though i was more confident using DP approach. so after solving with a DP approach first, i attemepted and solved with the "expand from the center" approach as well (11_10_2025_two_pointers.py).


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        ans_i = ans_j = 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n):  # palindrome with a single character
            dp[i][i] = True

        for i in range(n-1):    # checking palindrome with two characters
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1]:
                max_len = 2
                ans_i, ans_j = i, i + 1

        for d in range(3, n + 1):
            for i in range(n + 1 - d):
                j = i + d - 1
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j]:
                    max_len = d
                    ans_i, ans_j = i, j

        return s[ans_i:ans_j+1]

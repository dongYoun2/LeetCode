# problem.submission: https://leetcode.com/problems/longest-palindromic-substring/submissions/1723123285/
# runtime: 2476 ms, memory: 25.5 MB

# 26 min
# TC: O(n^2), where n is the length of the string
# SC: O(n^2) (2D dp array)


# From LeetCode Top Interview 150 - Multidimensional DP

# I knew that this problem is a dynamic programming problem, and kind of familiar with this problem. However, I also need to practice with center expansion method (two-pointer algorithm), which is another common approach (more efficient in terms of both time and space complexity) to solve this problem.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        if len(s) == 2:
            return s if s[0] == s[1] else s[0]

        dp = [[False] * len(s) for _ in range(len(s))]
        ans = s[0]

        # filling dp for a substring with length 1
        for i in range(len(s)):
            dp[i][i] = True

        # filling dp for a substring with length 2
        for i in range(len(s) - 1):
            dp[i][i+1] = (s[i] == s[i+1])

            if dp[i][i+1] and len(s[i:i+2]) > len(ans):
                ans = s[i:i+2]


        for k in range(2, len(s)):
            for i in range(len(s) - k):
                j = i + k
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])

                if dp[i][j] and len(s[i:j+1]) > len(ans):
                    ans = s[i:j+1]

        return ans


# notes while solving:

# s[i...j] is a palindrome (j - i >= 2)
# if
# 1) s[i+1...j-1] is a palindrome AND
# 2) s[i] == s[j]

# 초기 조건
# 1) single character: s[k] is always a palindrome
# 2) two characters: s[i...i+1] is a palindrome if s[i] == s[i+1]

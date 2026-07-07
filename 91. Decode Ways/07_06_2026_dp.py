# submission: https://leetcode.com/problems/decode-ways/submissions/2058110524/
# runtime: 0 ms (beats 100.00%), memory: 19.20 MB (beats 92.05%)
# 57 min (time including "07_06_2026_tle.py"; looked at the topic tag at 32 min)
# used bottom-up DP

# TC: O(n), where n is the length of the input string
# SC: O(n) (the dp array)


# the implementation is a little messy, especially for the base cases (initialization of the `dp[0]` and `dp[1]`). a cleaner bottom-up dp implementation can be found in the README.md.


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0 if s[0] == '0' else 1

        dp = [0] * n
        if s[0] != '0':
            dp[0] = 1
        
        if s[0] == '0' or ('3' <= s[0] <= '9' and s[1] == '0'):
            dp[1] = 0
        elif (s[:2] != '10' and s[:2] != '20') and ('11' <= s[:2] <= '26'):
            dp[1] = 2
        else:
            dp[1] = 1

        for i in range(2, n):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif '11' <= s[i-1:i+1] <= '26':
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]

        return dp[-1]

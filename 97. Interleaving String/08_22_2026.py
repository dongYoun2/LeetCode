# submission: https://leetcode.com/problems/interleaving-string/submissions/2116697800/
# runtime: 50 ms (beats 64.69%), memory: 19.39 MB (beats 72.52%)
# 28 min
# bottom up 2d dp approach

# tc: O(m*n), where m is the length of s1 and n is the length of s2
# sc: O(m*n)


# felt like a dp problem, so directly approached with 2d dp, but wasn't sure. in dp, the most important thing is to define the dp recurrence relation. i defined as dp[i][j] as whether s3[:i+j] is interleaved by s1[:i] and s2[:j]. then, the recurrence relation is dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1]).


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[0][0] = True

        for j in range(len(s2)):
            dp[0][j+1] = dp[0][j] and s2[j] == s3[j]

        for i in range(len(s1)):
            dp[i+1][0] = dp[i][0] and s1[i] == s3[i]
        
        for i in range(len(s1)):
            for j in range(len(s2)):
                dp[i+1][j+1] = (dp[i][j+1] and s1[i] == s3[i+j+1]) or (dp[i+1][j] and s2[j] == s3[i+j+1])


        for i in range(len(s1)+1):
            print(dp[i])


        return dp[-1][-1]

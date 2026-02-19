# submission: https://leetcode.com/problems/unique-paths/submissions/1924734956/
# runtime: 0 ms, memory: 19.41 MB
# 4 min

# TC: O(m*n), where m is the number of rows and n is the number of columns
# SC: O(n)


# solved using dynamic programming. after noticing this is a DP problem, i thought of using a 2D dp array, where space complexity is O(m*n. however, i realized the space can be optimized to O(n) by using a 1D dp array, and solved with that.


# cf.) note that this problem can also be solved using combinatorics. every path  is just a different ordering of down and right moves. since there are m-1 down moves and n-1 right moves, total moves would be (m-1) + (n-1) = m+n-2. now we need to choose (m-1) positions to place the down moves, then the rest would be automatically determined to be the right moves. therefore, the answer is simply (m+n-2) choose (m-1) or (m+n-2) choose (n-1). the submitted code can be found here: https://leetcode.com/problems/unique-paths/submissions/1248920334/.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i-1]

        return dp[-1]

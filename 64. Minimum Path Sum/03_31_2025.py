# problem: https://leetcode.com/problems/minimum-path-sum/
# submission: https://leetcode.com/problems/minimum-path-sum/submissions/1592289769/

# 5 min
# TC: O(m*n)
# SC: O(m*n) (Although this can be optmized to O(1) if store the dp values in the 'grid' itself (in-place), but I believe that is not a good practice)

# This problem is also a very typical dynamic programming problem. The space complexity can be reduced to O(n) by keeping a 1D array of size 'n' since we only need the upper value from the previous row (dp[i]) and the left value from the same row (dp[i-1]).


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # 0-th row
        for c in range(1, n):
            dp[0][c] = dp[0][c-1] + grid[0][c]

        # 0-th column
        for r in range(1, m):
            dp[r][0] = dp[r-1][0] + grid[r][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]

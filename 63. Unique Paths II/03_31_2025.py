# problem: https://leetcode.com/problems/unique-paths-ii/submissions/
# submission: https://leetcode.com/problems/unique-paths-ii/submissions/1592327982/

# 10 min
# TC: O(m*n)
# SC: O(m*n) (space complexity cna be reduced to O(1) by using in-place modificuations of the input)

# Typical dynamic programming problem.


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        EMPTY, OBSTACLE = 0, 1

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == EMPTY else 0

        # 0-th row
        for c in range(1, n):
            dp[0][c] = dp[0][c-1] if obstacleGrid[0][c] == EMPTY else 0

        # 0-th column
        for r in range(1, m):
            dp[r][0] = dp[r-1][0] if obstacleGrid[r][0] == EMPTY else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == EMPTY:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0


        return dp[-1][-1]

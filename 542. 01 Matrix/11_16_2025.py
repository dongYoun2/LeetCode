# submission: https://leetcode.com/problems/01-matrix/submissions/1831005644/
# runtime: 47 ms, memory: 91.88 MB

# 19 min
# TC: O(m*n)
# SC: O(1) (answer array is not considered)


# from Grind 128 questions

# didn't know which algorithm to use at first, but noticing that when iterate from top-left to bottom-right, we can update the current cell's distance considering the cells we have already visited. to do this, we can simply use a dp array and consider the top and left cell. likewise, after that, we can simply iterate backward (from bottom-right to top-left) in dp array to consider the bottom and right cell, which eventually take into account all cells (or all four directions).

# cf.) note that this problem can also be solved by bfs, similar to the idea of the topological sorting. for bfs solution, refer to the markdown file.


import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[math.inf] * n for _ in range(m)]

        # first pass: dp from top-left -> bottom-right
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        continue
                    elif i == 0:
                        dp[i][j] = dp[i][j-1] + 1
                    elif j == 0:
                        dp[i][j] = dp[i-1][j] + 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

        # second pass: dp from bottom-right -> top-left
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if dp[i][j] == 0:
                    continue
                else:
                    if i == m-1 and j == n-1:
                        continue
                    elif i == m-1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
                    elif j == n-1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                    else:
                        dp[i][j] = min(dp[i][j], dp[i+1][j] + 1, dp[i][j+1] + 1)

        return dp


# notes while solving:
# e.g.
# 0 1 0
# 1 1 0
# 1 1 1

# first pass:
# 0 1 0
# 1 2 0
# 2 3 1

# second pass:
# 0 1 0
# 1 1 0
# 2 2 1

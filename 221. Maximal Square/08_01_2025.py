# submission: https://leetcode.com/problems/maximal-square/submissions/1719833561/
# runtime: 113 ms, memory: 33 MB

# 21 min
# TC: O(m * n), where m is the number of rows and n is the number of columns in the matrix.
# SC: O(m * n), for the dp table. (can make it to O(1) by updating the matrix in place, but i believe it's not the best practice.)

# From LeetCode Top Interview 150 - Multidimensional DP

# i defined dp[r][c] as the length of one side of the largest square whose bottom-right corner is at (r, c).

# in the beginning, i simply checked if all values in three directions (left, up, diag) are the same for the case when matrix[r][c] == '1'. however, that's wrong due to the below counter example:
# matrix = [
#     ["1","1","1","1","0"],
#     ["1","1","1","1","0"],
#     ["1","1","1","1","1"],
#     ["1","1","1","1","1"],
#     ["0","0","1","1","1"]
#     ]
# answer: 16

# then, the dp array becomes:
# [1, 1, 1, 1, 0]
# [1, 2, 1, 2, 0]
# [1, 1, 1, 1, 1]
# [1, 2, 1, 2, 1]
# [0, 0, 1, 1, 1]

# where it supposed to be (correct one):
# [1, 1, 1, 1, 0]
# [1, 2, 2, 2, 0]
# [1, 2, 3, 3, 1]
# [1, 2, 3, 4, 2]
# [0, 0, 1, 2, 3]


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        # fill out the first row
        for c in range(n):
            dp[0][c] = int(matrix[0][c])

        # fill out the first col
        for r in range(m):
            dp[r][0] = int(matrix[r][0])

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == '0':
                    dp[r][c] = 0
                else:   # '1'
                    left, up, diag = dp[r][c-1], dp[r-1][c], dp[r-1][c-1]
                    if left >= 1 and up >= 1 and diag >= 1:
                        dp[r][c] = min(left, up, diag) + 1
                    else:
                        dp[r][c] = 1

        return max(e for row in dp for e in row) ** 2

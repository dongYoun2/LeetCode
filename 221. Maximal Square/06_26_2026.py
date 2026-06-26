# submission: https://leetcode.com/problems/maximal-square/submissions/2047209904/
# runtime: 122 ms (beats 28.11%), memory: 33.27 MB (beats 27.77%)
# 16 min
# solved using DP

# refer to the 08_01_2025.py for a complexity analysis.


# this is a typical 2d DP problem. i remeber this problem while watching the google coding interview video, lol: https://youtu.be/Ti5vfu9arXQ?si=wU6RLtMb2AQcpsI7 


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[int(e) for e in row] for row in matrix]

        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 1:
                    dp[i][j] = min((dp[i-1][j-1], dp[i-1][j], dp[i][j-1])) + 1
        
        return max(e**2 for r in dp for e in r)

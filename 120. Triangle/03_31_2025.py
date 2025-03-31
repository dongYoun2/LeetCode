# problem: https://leetcode.com/problems/triangle/
# submission: https://leetcode.com/problems/triangle/submissions/1592271727/

# 12 min
# TC: O(1 + 2 + 3 + ... + n) -> O(n*(n+1)/2) -> O(n^2), where n is the number of rows in the triangle
# SC: O(2*n) -> O(n) (each 'dp' and 'prev_dp' has a space complexity of O(n))

# This problem is also a typical DP problem. As soon as you find the recurrence relation, implementation is not too difficult. One thing to notice is that although the given input is 2D, we can use 2 1D arrays to store the previous and current rows. This is because we only need the previous row to calculate the current row. (At first, I used one 1D array and figured out that the array became overlapped when I calculated the current row lol)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        dp = [float('inf')] * n

        dp[0] = triangle[0][0]

        for i in range(1, n):
            row = triangle[i]
            dp_prev = dp.copy()

            dp[0] += row[0] # first element
            dp[len(row)-1] = dp_prev[len(row)-2] + row[-1]   # last element

            for j in range(1, len(row) - 1):
                dp[j] = min(dp_prev[j-1], dp_prev[j]) + row[j]

        return min(dp)

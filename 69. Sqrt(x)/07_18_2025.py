# submission: https://leetcode.com/problems/sqrtx/submissions/1702617693/
# runtime: 1098 ms, memory: 17.6 MB

# 6 min
# TC: O(n // 2) -> O(n), where n is the input number x
# SC: O(1)

# From LeetCode Top Interview 150 - Math

# solved it in a linear time. however, this can be optimized to O(log n) using binary search.


class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        for n in range(x // 2 + 2):
            if n * n > x:
                break
            ans = n

        return ans

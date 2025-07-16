# submission: https://leetcode.com/problems/number-of-1-bits/submissions/1700362066/
# runtime: 0 ms, memory: 17.9 MB

# 1 min
# TC: O(1), technically O(b) where b is the number of bits in n, but since n is always 1 <= n <= 2^31 - 1 given in the problem condition, b is constant.
# SC: O(1)

# From LeetCode Top Interview 150 - Bit Manipulation


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n:
            last_bit = n & 1
            ans += last_bit
            n >>= 1

        return ans

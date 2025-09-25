# submission: https://leetcode.com/problems/house-robber/submissions/1781882713/
# runtime: 0 ms, memory: 17.70 MB

# 6 min
# TC: O(n), where n is the length of nums
# SC: O(n), for dp array


# From LeetCode Top Interview 150 - 1D DP

# in the last return statement, i don't need to return max(dp[-1], dp[-2]). Instead, i can simply return dp[-1] because it's guaranteed to be the maximum value (so dp[-1] >= dp[-2]).


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return max(dp[-1], dp[-2])

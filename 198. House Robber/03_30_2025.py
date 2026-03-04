# submission: https://leetcode.com/problems/house-robber/submissions/1591435417/
# runtime: 0 ms (beats 100.00%), memory: 17.70 MB (beats 95.11%)
# 7 min

# TC: O(n)
# SC: O(n)

# Typical dynamic programming problem. Below code can be improved to O(1) space complexity by using two variables instead of a dp array.


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = nums[0]

        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]


# notes while solving:
# dp[i] = max(dp[i-2] + nums[i], dp[i-1])

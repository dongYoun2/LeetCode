# submission: https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1654337044/

# 35 min

# This is the very first attempt, but it's wrong.


import math

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        smallest = min(nums)
        sm_idx = nums.index(smallest)
        sm_indices = [i for i in range(n) if nums[i] == nums[sm_idx]]

        ans = -math.inf
        for sm_idx in sm_indices:
            start = (sm_idx + 1) % n

            ans = curr_sum = nums[start]
            for i in range(start + 1, start + len(nums)):
                j = i % n
                curr_sum = max(curr_sum + nums[j], nums[j])
                ans = max(ans, curr_sum)

        return ans

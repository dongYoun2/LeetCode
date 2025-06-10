# submission: https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1659176356/
# Time Limit Exceeded

# 20 min
# TC: O(n^2), where n is the length of the input array.
# SC: O(1)

# This is a brute force solution that checks all possible starting points for the subarray. For each starting point, we run the Kadane's algorithm.

import math

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        assert n > 0

        ans = -math.inf
        for i in range(n):
            local_ans = curr_sum = nums[i]

            for j in range(i + 1, (i + 1) + n - 1):
                j %= n
                curr_sum = max(curr_sum + nums[j], nums[j])
                local_ans = max(local_ans, curr_sum)

            ans = max(ans, local_ans)

        return ans


# notes while solving:
#  1 -2 3 -2  -> 3

#  -2 3 -2 1 -> 3

#  3 -2 1 -2  -> 3

# -2 1 -2 3   -> 3


# 5 -3 5  -> 7

# -3 5 5  -> 10

# 5 5 -3  -> 10

# submission: https://leetcode.com/problems/maximum-subarray/submissions/1652142594/
# runtime: 92 ms, memory: 32.79 MB

# 8 min
# TC: O(n), where n is the length of the input array.
# SC: O(1)


# From LeetCode Top Interview 150 - Kadane's Algorithm

# It's my third time solving this problem (first: 04/07/2024, second: 11/25/2024).

# Kadane's Algorithm is essentially a dynamic programming approach that finds the maximum sum of a contiguous subarray in linear time.

# cf.) For the solution to the follow-up question, refer to the markdown file.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert len(nums) > 0

        ans = curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            ans = max(ans, curr_sum)

        return ans

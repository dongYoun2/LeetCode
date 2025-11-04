# from re import I


# submission: https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1819935527/
# Time Limit Exceeded


# 57 min (looked at till the second hint)
# TC: O(n^2), where n is the length of the nums
# SC: O(n)


# the logic is correct that I considered two cases, where 1) the maximum subarray is not circular, which can be solved by Kadane's algorithm (maximum subarray sum), and 2) the maximum subarray crosses the boundary of the array.

# however, due to the `max(suffix_sum[i:])` and `max(prefix_sum[:i])` operations in the for loop, the code below takes O(n^2) time, which is actually the same as the brute-force solution. to prevent this, i can precompute either the maximum suffix sum (or the maximum prefix sum) for each index in the array using the dynamic programming approach. for more details, refer to the markdown file (this method corresponds to the first approach in the README.md).


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(0, curr_sum) + nums[i]
            max_sum = max(max_sum, curr_sum)

        prefix_sum, suffix_sum = [0] * len(nums), [0] * len(nums)
        prefix_sum[0], suffix_sum[-1] = nums[0], nums[-1]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        for i in range(len(nums) - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + nums[i]

        buf_sz = len(nums)
        max_sum2 = max(prefix_sum)
        for i in range(1, buf_sz):
            sub_sum = max(suffix_sum[i:]) + max(prefix_sum[:i])
            max_sum2 = max(max_sum2, sub_sum)

        return max(max_sum, max_sum2)

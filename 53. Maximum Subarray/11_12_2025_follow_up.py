# submission: https://leetcode.com/problems/maximum-subarray/submissions/1827944031/
# runtime: 262 ms, memory: 45.83 MB
# solves the follow-up question.

# 21 min
# complexity analysis is mentioned in the "follow_up.md" file.


# the code below is the exact the same implementation shown in the second code of the "follow_up.md" file. may be the best solution for the divide and conquer approach in terms of the runtime in practice.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide(l, r):
            if l == r:
                x = nums[l]
                return x, x, x, x    # max_sum, total_sum, max_prefix_sum, max_suffix_sum

            m = (l + r) // 2
            l_max, l_total, l_prefix, l_suffix = divide(l, m)
            r_max, r_total, r_prefix, r_suffix = divide(m + 1, r)
            return max(l_max, r_max, l_suffix + r_prefix), l_total + r_total, max(l_prefix, l_total + r_prefix), max(r_suffix, r_total + l_suffix)

        return divide(0, len(nums) - 1)[0]

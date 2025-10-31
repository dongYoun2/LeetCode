# submission: https://leetcode.com/problems/maximum-subarray/submissions/1817026351/
# runtime: 499 ms, memory: 45.36 MB
# the code below solves the follow-up question.

# 17 min
# TC: O(n log n), where n is the length of nums
# SC: O(log n), for the recursion stack (O(n) for the slicing for optimized in CPython)


# the solution below is fairly straightforward. the key is to divide the array into two halves, and then find the maximum subarray sum in each half. the maximum subarray sum is either 1) the maximum subarray sum in the left half (`l_best`), 2) the maximum subarray sum in the right half (`r_best`), or 3) the maximum subarray sum that crosses the midpoint (`l_suffix + r_prefix`).

# cf.) note that although we use slicing to compute the maximum prefix sum (`prefix)` and the maximum suffix sum (`suffix`), the runtime is 2.5x faster than the first code (https://leetcode.com/problems/maximum-subarray/submissions/1652234138/) in the follow-up.md. this is because the slicing is optimized in CPython due to C-optimized sum.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def compute(s, e):
            if s == e:
                # return (max_prefix, max_suffix, max_subarray)
                return nums[s], nums[s], nums[s]

            m = (s + e) // 2
            l_prefix, l_suffix, l_best = compute(s, m)
            r_prefix, r_suffix, r_best = compute(m + 1, e)

            prefix = max(l_prefix, sum(nums[s:m+1]) + r_prefix)
            suffix = max(r_suffix, sum(nums[m+1:e+1]) + l_suffix)
            best = max(l_best, r_best, l_suffix + r_prefix)

            return prefix, suffix, best


        return compute(0, len(nums) - 1)[2]

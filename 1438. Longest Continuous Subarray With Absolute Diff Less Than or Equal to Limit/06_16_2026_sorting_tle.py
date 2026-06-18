# submission: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/2035648527/
# time limit exceeded
# 20 min

# TC: O(n^2 log n)
# - O(n) for a sliding window
# - O(n log n) for sorting (the window)
# SC: O(n) (1. temporary space for sorting the window, 2. python slicing for the window)


# chose from a neetcode "sliding window" category.

# i expected this solution to be time limit exceeded, but still i tried it. while using a lazy sliding window technique (since the problem requires to find the longest subarray), the key issue is how to find the minimum and maximum values of the current window efficiently. considering the problem constraint that the maximum length of the array is 100K, we need to solve in O(n log n) time.

# so, instead of brute-force finding (either using sorting or linear scan), i considered using heap but couldn't figure out updating heap when the window slides. hence, i simply submitted the code below, which is the "lazy sliding window + sorting-based min/max recomputation" approach.

# cf.) performing linear scan for finding min/max values for each window is slightly better than sorting since the TC is O(n^2).


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        sm = lg = nums[0]
        l = 0
        ans = 1
        for r in range(1, n):
            lg = max(lg, nums[r])
            sm = min(sm, nums[r])

            if lg - sm <= limit:
                ans = max(ans, r - l + 1)
            else:
                if nums[l] == lg or nums[l] == sm:
                    sorted_window = sorted(nums[l+1:r+1])
                    sm, lg = sorted_window[0], sorted_window[-1]

                l += 1
        
        return ans

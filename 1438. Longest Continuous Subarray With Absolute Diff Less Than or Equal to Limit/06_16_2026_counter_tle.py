# submission: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/2035657965/
# time limit exceeded
# 43 min (includes time writing "06_16_2026_sorting_tle.py" and "06_16_2026_heap_wrong.py")

# TC: O(n*k), where n is the length of the array and k is the number of unique elements in the array (worst case: k = n --> O(n^2))
# SC: O(k) (worst case: k = n --> O(n))


# chose from a neetcode "sliding window" category.

# just like the "06_16_2026_sorting_tle.py", also expected this solution to be time limit exceeded.

# instead of pure sorting and pure linear scan of the window, i tried the frequency-based approach, which allows to linearly search the min/max values only among the unique elements of the window. however, the worst case time complexity is still O(n^2), which would be the same as the pure linear scan (of the window) approach.


from collections import Counter

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        sm = lg = nums[0]
        cntr = Counter([nums[0]])
        l = 0
        ans = 1
        for r in range(1, n):
            cntr[nums[r]] += 1
            lg = max(lg, nums[r])
            sm = min(sm, nums[r])

            if lg - sm <= limit:
                ans = max(ans, r - l + 1)
            else:
                cntr[nums[l]] -= 1
                if cntr[nums[l]] == 0:
                    del cntr[nums[l]]

                    if nums[l] == sm:
                        sm = min(cntr.keys())
                    if nums[l] == lg:
                        lg = max(cntr.keys())

                l += 1
        
        return ans

# problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# submission: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1590310441/

# 5 min

import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        s = bisect.bisect_left(nums, target)
        if s >= len(nums) or nums[s] != target:
            return [-1, -1]

        e = bisect.bisect(nums, target)

        return [s, e - 1]

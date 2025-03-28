# problem: https://leetcode.com/problems/search-insert-position/
# submission: https://leetcode.com/problems/search-insert-position/submissions/1589423600/

# 3 min
# TC: O(log n) (required in the problem)
# SC: O(1)

# Typical binary search problem. Since the input array contains distinct numbers, the solution is equivalent to `return bisect.bisect_left(nums, target)`.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            med = l + (r - l) // 2 # prevent overflow

            if nums[med] == target:
                return med
            elif target > nums[med]:
                l = med + 1
            else:
                r = med - 1

        return l

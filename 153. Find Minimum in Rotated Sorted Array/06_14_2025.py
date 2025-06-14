# submission: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1663497434/

# 12 min
# TC: O(log n), where n is the number of elements in the array.
# SC: O(1)


# From LeetCode Top Interview 150 - Binary Search

# Typical binary search problem with a twist due to the rotation. The instruction that we have to write the alogrithm in O(log n) time complexity is a hint that we should use binary search.


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2

            if m < r and nums[m] > nums[m+1]:
                return nums[m+1]
            elif l < m and nums[m-1] > nums[m]:
                return nums[m]
            elif nums[l] >= nums[m] or nums[l] <= nums[m] <= nums[r]:   # second cluase of 'or' means no rotation
                r = m - 1
            elif nums[m] >= nums[r]:
                l = m + 1

        return nums[l]


# notes while solving:
# 17 11 12 13 15

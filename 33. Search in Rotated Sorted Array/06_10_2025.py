# submission: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1659752261/

# 29 min
# TC: O(log n), where n is the number of elements in the array.
# SC: O(1)

# From LeetCode Top Interview 150 - Binary Search

# It's important to understand that the array is sorted and rotated, which means that it was originally sorted but then shifted at some pivot point. The key is to determine which part of the array is sorted and where the target might be located.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            med = (left + right) // 2

            if nums[med] == target:
                return med

            if med - 1 >= left and nums[left] <= nums[med-1]:   # pivot is in right part
                if nums[left] <= target <= nums[med-1]:
                    right = med - 1
                else:
                    left = med + 1
            elif med + 1 <= right and nums[med+1] <= nums[right]:   # pivot is in left part
                if nums[med+1] <= target <= nums[right]:
                    left = med + 1
                else:
                    right = med - 1
            else:
                return -1

        return -1

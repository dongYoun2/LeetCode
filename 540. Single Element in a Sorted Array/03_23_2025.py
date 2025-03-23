# https://leetcode.com/problems/single-element-in-a-sorted-array/

# 37 min (Spent some time on understanding how the `bisect_left()` and `bisect_right()` works when there are many repeated values, but eventually didn't use these built-in functions.)
# TC: O(log n)
# SC: O(1)
# Solving the problem with the above complexities was required from the problem statement.

# Since the array is sorted, I assumed that I had to use binary search somehow. (If it's not sorted, I believe the XOR bitwise solution could solve the problem in O(n) time complexity and O(1) space complexity.) The core idea is to how decide whether the single element is in the left subarray or right subarray after bisecting based on the med point.

# cf.) At first, I forgot to consider the `med` is the exact matching single element.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            med_idx = l + (r - l) // 2 # prevent index overflow

            if nums[med_idx] == nums[med_idx+1]:
                r1, l1 = r, med_idx + 2
                r2, l2 = med_idx - 1, l
            elif nums[med_idx] == nums[med_idx-1]:
                r1, l1 = r, med_idx + 1
                r2, l2 = med_idx - 2, l
            else:  # found
                return nums[med_idx]

            if (r1 - l1 + 1) % 2 == 1:
                l, r = l1, r1
            else:
                l, r = l2, r2

        assert l == r
        return nums[l]

# notes solving this problem

# elements num 홀수 개
# 1 1 3 3 5
# 1 1 3 3 5 7 7
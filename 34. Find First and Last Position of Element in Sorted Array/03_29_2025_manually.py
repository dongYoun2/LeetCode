# problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# submission: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1590349967/

# 31 min
# TC: O(log n)
# SC: O(1)

# Typical binary search problem with duplicate numbers. Manually implementing this was quite tricky, especially finding a correct index. I have to simulate the arrays with lengths 1, 2, 3, and 4 (manageable lengths as well as both odd and even lengths). For me, binary search is always confusing in deciding between `while l < r` or `while l <= r` and between equality inclusion or exclusion in the target value comparison inequality (i.e. `if nums[m] >= target`).

import math

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # find left-most index
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2

            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        assert l == r
        assert l < len(nums) # valid index

        if nums[l] != target:
            return [-1, -1]

        left_most_idx = l

        # find right-most index
        l, r = 0, len(nums) - 1
        while l < r:
            m = math.ceil((l + r) / 2)

            if nums[m] <= target:
                l = m
            else:
                r = m - 1

        assert l == r

        right_most_idx = l

        return [left_most_idx, right_most_idx]

# notes while solving:
# 10 20
# 1 5 5 5 5 5 10
# 3 3 3 3
# 5 7 7 8 8 10
#         l r
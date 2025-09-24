# submission :https://leetcode.com/problems/sort-colors/submissions/1780373481/
# runtime: 0 ms, memory: 17.75 MB

# 5 min
# TC: O(n), where n is the number of elements in nums
# SC: O(1)

# this is a two-pass approach. the logic is straightforward and is the same as the solution in 04_25_2024.py.

from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        cntr = Counter(nums)
        red_cnt, white_cnt, blue_cnt = cntr[0], cntr[1], cntr[2]

        for i in range(red_cnt):
            nums[i] = 0

        for i in range(red_cnt, red_cnt + white_cnt):
            nums[i] = 1

        for i in range(red_cnt + white_cnt, red_cnt + white_cnt + blue_cnt):
            nums[i] = 2

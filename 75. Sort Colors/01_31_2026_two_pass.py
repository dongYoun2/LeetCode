# submission: https://leetcode.com/problems/sort-colors/submissions/1903618166/
# runtime: 0 ms (Beats 100.00%), memory: 19.27 MB (Beats 42.28%)
# 2 min

# time and space complexity is the same as the markdown file's solution. the only difference is that this approach solves in two passes.


# conceptually, this code's logic is the same as the '04_25_2024.py' and '09_23_2025.py' solutions. the only difference is that this one stores counts in pointer variables, whereas the others store in a counter.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1

        for i, n in enumerate(nums):
            if n == 0:
                l += 1
            elif n == 2:
                r -= 1
            
        for i in range(l):
            nums[i] = 0
        
        for i in range(l, r + 1):
            nums[i] = 1
        
        for i in range(r + 1, len(nums)):
            nums[i] = 2

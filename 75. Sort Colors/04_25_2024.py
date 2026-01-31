# submission: https://leetcode.com/problems/sort-colors/submissions/1780744894/
# runtime: 0 ms, memory: 17.76 MB

# TC: O(n), where n is the number of elements in nums
# SC: O(1) (in this problem, counter takes O(1) space since there are only 3 (constant) colors)


# the solution below meets time and space complexities mentioned in the follow-up question, but it's a two-pass approach.


from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cntr = Counter(nums)

        i = 0
        while i < len(nums):
            for color in range(3):
                for _ in range(cntr[color]):
                    nums[i] = color
                    i += 1

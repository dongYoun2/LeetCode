# problem: https://leetcode.com/problems/two-sum/
# submission: https://leetcode.com/problems/two-sum/submissions/1610062470/

# TC: O(n), where n is the length of the input list
# SC: O(n) (hashmap)

# From LeetCode Top Interview 150 - Hashmap

# This is a classic problem that can be solved using a hashmap. I have solved it several times before. The code below also meets the criteria for the follow-up question, which requires the solution to be in O(n) time complexity.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, n in enumerate(nums):
            n_other = target - n

            if n_other in hash:
                return [hash[n_other], i]

            hash[n] = i

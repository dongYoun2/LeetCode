# problem: https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/
# spent around 30 min but could not solve this problem.


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

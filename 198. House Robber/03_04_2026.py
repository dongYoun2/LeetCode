# submission: https://leetcode.com/problems/house-robber/submissions/1938080412/
# runtime: 0 ms (beats 100.00%), memory: 19.42 MB (beats 22.98%)
# 7 min

# TC: O(n), where n is the length of nums
# SC: O(1) (two variables)


# typical dynamic programming problem.

# note that instead of using 1D dp array, we can simply use two variables to solve.

# also, we don't even need the early return check. refer to this submission: https://leetcode.com/problems/house-robber/submissions/1555078213/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        a = nums[0]
        b = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            a, b = b, max(a + nums[i], b)

        return b

# submission: https://leetcode.com/problems/jump-game-ii/submissions/1735970675/
# runtime: 310 ms, memory: 18.51 MB

# 12 min
# TC: O(n^2), where n is the length of nums
# SC: O(n)


# From LeetCode Top Interview 150 - Array / String

# i solved this problem using dynamic programming iterating backward. just like the "55. Jump Game" problem, it's more straightforward to loop in the reverse direction. dp[i] represents the minimum number of jumps needed to reach the end from index i.

# however, the below code can be slightly improved by inializing dp array float('inf') or the maximum possible value. this way, we can avoid checking the case where nums[i] is 0 (or equivalent to checking if i == i + jump_range).

# for more details, refer to the markdown file.


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n - 2, -1, -1):
            jump_range = nums[i]
            if i == i + jump_range: # equivalent to `if nums[i] == 0`
                dp[i] = float('inf')
                continue

            dp[i] = min(dp[i+1:i+jump_range+1]) + 1

        return dp[0]

# submission: https://leetcode.com/problems/jump-game/submissions/1732333203/
# runtime: 1650 ms, memory: 18.6 MB

# 7 min
# TC: O(n^2), where n is the length of nums
# SC: O(n), for dp array


# From LeetCode Top Interview 150 - Array / String

# after submitting `08_12_2025.py`, i realized this problem can also be solved using dynamic programming. it's prettty straightforward when the array is looped backward. `dp[i]` indicates whether we can reach the end from index `i`. if we can reach the end from any index `j` that is reachable from `i` (so the range of `j` is from `i` to `i + nums[i] + 1`.), then `dp[i]` is set to True.

# for additional bottom-up and top-down (with memoization) approaches, refer to the editorial section.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, i + nums[i] + 1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]

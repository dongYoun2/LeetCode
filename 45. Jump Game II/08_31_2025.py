# submission: https://leetcode.com/problems/jump-game-ii/submissions/1754967139/
# runtime: 307 ms, memory: 18.6 MB

# 14 min
# TC: O(n^2), where n is the length of nums
# SC: O(n), dp array


# From LeetCode Top Interview 150 - Array / String

# i knew this problem could be solved using a greedy approach, but i first attempted with DP solution. One trivial but important thing to notice is that using `min(dp[i+k] for k in range(1, nums[i] + 1))` instead of `min(dp[i:i+nums[i]+1])` fails for the case "nums = [2,1]" because dp[2] is out of range. (my first submission failed since i didn't take this into account.)


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10002] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            if nums[i] != 0:
                dp[i] = min(dp[i:i+nums[i]+1]) + 1

        return dp[0]


# notes while solving:
# dp[i] represents the min num of jums to reach from index i to the end index n - 1
# dp[i] = min(dp[i+k] for k in range(1, nums[i] + 1)) + 1 (0 <= i < n-1)

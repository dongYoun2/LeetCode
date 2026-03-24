# submission: https://leetcode.com/problems/longest-increasing-subsequence/submissions/1592202342/
# runtime: 1752 ms (beats 12.02%), memory: 18.11 MB (beats 100.00%)
# 7 min (the reason i could solve quite fast is because i had solved the same problem a week ago—02/24/2025)

# TC: O(n^2), where n is the length of nums
# SC: O(n)

# This is the second time solving this problem, which I first solved on 02/24/2025. Since the range of n is less than or equal to 2500, the time complexity of O(n^2) is also acceptable. This problem is also a typical dynamic programming question.

# Using binary search, the time complexity can be improved to O(n log n). For more details, refer to the LeetCode Editorial's "Approach 2: Intelligently Build a Subsequence" and "Approach 3: Improve With Binary Search." These are very refreshing and interesting solutions.


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1] * l

        for curr in range(l):
            for prev in range(curr):
                if nums[prev] < nums[curr]:
                    dp[curr] = max(dp[curr], dp[prev] + 1)

        return max(dp)

# notes while solving:
# n <= 2500

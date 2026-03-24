# submission: https://leetcode.com/problems/longest-increasing-subsequence/submissions/1957757408/
# runtime: 1249 ms (beats 49.93%), memory: 19.47 MB (beats 76.38%)
# 21 min

# time and space complexities are the same as the 03_31_2025.py. refer to that for details.


# noticing that n can be at most 2.5K, i assumed that the solution needs to be at most O(n^2). i also assumed that this could be solved using a dynamic programming approach (idk why but somehow in my subconscious, i remember that LIS problem was a dp problem).

# cf.) once i solved with the dp approach, i attempted a follow-up question, which requires to solve in O(n log n) time. however, after thinking about it for around 10 minutes, i couldn't figure it out.


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            cand = max((dp[k] for k in range(i) if nums[k] < nums[i]), default=0)
            dp[i] = cand + 1

        return max(dp)

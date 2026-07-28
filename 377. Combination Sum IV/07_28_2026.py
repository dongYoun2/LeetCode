# submission: https://leetcode.com/problems/combination-sum-iv/submissions/2085036799/
# runtime: 49 ms (beats 63.74%), memory: 19.45 MB (beats 13.47%)
# 14 min
# solved using dynamic programming

# TC: O(target * n), where n is the length of `nums`
# SC: O(target)


# this is a typical dp problem; very similar to the coin change problem.


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if i-num < 0:
                    break
                dp[i] += dp[i-num]

        return dp[target]


# notes while solving:
# 1 2 3 4
# 1 2 4 7

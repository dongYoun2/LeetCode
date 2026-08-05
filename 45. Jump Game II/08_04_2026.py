# submission: https://leetcode.com/problems/jump-game-ii/submissions/2094622324/
# runtime: 3246 ms (beats 7.27%), memory: 20.03 MB (beats 65.36%)
# 11 min
# solved using forward dp

# refer to the README.md's "Iterating Forward" section for the complexirty analysis


# noticing from the input constraints, i assumed there may be a O(n) time solution. i suspected greedy algorithm but wasn't sure. so i simply appraoched with the dp solution, which is obvious algorithm for this jump game series problem. looking at the runtime graph once i submitted this code, i was confident that there is a O(n) solution. hence, i also solved with a greedy algorithm in 08_04_2026_greedy.py.


import math


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n
        dp[0] = 0
        for i in range(n-1):
            for j in range(1, nums[i]+1):
                pos = min(i+j, n-1)
                dp[pos] = min(dp[pos], dp[i]+1)

        return dp[-1]

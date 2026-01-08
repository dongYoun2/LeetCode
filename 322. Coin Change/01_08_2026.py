# submission: https://leetcode.com/problems/coin-change/submissions/1879101373/
# runtime: 443 ms, memory: 19.7 MB

# 17 min
# refer to the 03_31_2025.py for a complexity analysis.


# The solution below exactly reflects two improvements mentioned in the 03_31_2025.py.


import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [math.inf] * amount
        
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i-c] + 1)
        
        return dp[amount] if dp[amount] != math.inf else -1

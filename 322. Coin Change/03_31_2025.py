# problem: https://leetcode.com/problems/coin-change/
# submission: https://leetcode.com/problems/coin-change/submissions/1592174618/

# 10 min
# TC: O(n*m), where n is the amount, and m is the number of coin denominations
# SC: O(n)

# This problem is also a popular dynamic programming problem. By looping over 'coins' first instead of the 'amount', we can remove the 'i-c >= 0' check in the if condition. Also, by initializing dp with float('inf') (or maximum number + 1 that cannot be reached), we can avoid the 'dp[i-c] != -1' check in the if condition. Therefore, we can simplify the code and make it more readable. (These changes additionally allow us to remove the second if condition, where we check if the cands are empty.) For more details, refer to the Editorial section's Approach 3 (DP - bottom-up).


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            cands = []
            for c in coins:
                if i - c >= 0 and dp[i-c] != -1:
                    cands.append(dp[i-c])

            if not cands:
                continue

            dp[i] = min(cands) + 1


        return dp[amount]


# notes while solving:
# dp[i]: fewest num of coins to make up amount 'i'

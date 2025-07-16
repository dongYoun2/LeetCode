# submission: https://leetcode.com/problems/number-of-1-bits/submissions/1700363355/
# runtime: 3 ms, memory: 17.7 MB

# 1 min
# TC: O(1)
# SC: O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n:
            n, r = divmod(n, 2)
            ans += r

        return ans

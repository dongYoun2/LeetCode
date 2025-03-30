# problem: https://leetcode.com/problems/climbing-stairs/
# submission: https://leetcode.com/problems/climbing-stairs/submissions/1591404489/

# 4 min
# TC: O(n)
# SC: O(1)

# Typical Dynamic Programming problem. Exactly the same as Fibonacci numbers. Below is the iterative solution.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        n1, n2 = 1, 2

        for _ in range(2, n):
            n1, n2 = n2, n1 + n2

        return n2

# notes while solving:
# 점화식: climbs[n] = climbs[n-1] + climbs[n-2]

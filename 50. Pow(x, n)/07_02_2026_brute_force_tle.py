# submission: https://leetcode.com/problems/powx-n/submissions/2053507237/
# Time Limit Exceeded
# 12 min
# naive exponentiation approach

# TC: O(n), where n is the exponent 'n' in the function myPow(...).
# SC: O(1)


# at first, i didn't consider the range of n, which can be at most 2^31 - 1. so i simply implemented a brute-force linear time solution, which is TLE, though the logic was correct.


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        
        if x == 1.0:
            return 1.0
        
        n_abs = abs(n)

        ans = 1
        while n_abs > 0:
            ans *= x
            n_abs -= 1
        
        return float(ans) if n > 0 else 1 / ans

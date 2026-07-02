# submission: https://leetcode.com/problems/powx-n/submissions/2053528190/
# runtime: 0 ms (beats 100.00%), memory: 19.55 MB (beats 18.76%)
# 34 min (time includes solving "07_02_2026_brute_force_tle.py")
# solved using divide-and-conquer / binary exponentiation (iterative approach)

# complexity analysis is the same as the "07_19_2025.py".


# for logic and details, refer to the comments in the "07_19_2025.py" file.


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        
        if x == 1.0:
            return 1.0

        twos = list(bin(abs(n))[2:])
        twos.reverse()
        exps = [i for i, c in enumerate(twos) if c == '1']


        def pow_(base, exp):
            res = base

            while exp > 0:
                res *= res
                exp -= 1
            
            return res


        ans = 1.0
        for e in exps:
            ans *= pow_(x, e)

        return ans if n > 0 else 1 / ans

# submission: https://leetcode.com/problems/reverse-integer/submissions/2060826436/
# runtime: 51 ms (beats 24.72%), memory: 19.10 MB (beats 92.45%)
# 44 min

# TC: O(log x), where x is the input integer (log with base 10)
# SC: O(1)


# i first considered converting the integer to a string, but directly noticed that it's not doable due to the integer overflow constraints mentioned in the problem description—"Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."

# then i came up with division and modulo operations. one important fact is that the python's division and modulo behaves differently from other languages, such as C++ or Golang, when either dividend or divisor is negative. the former follows the floor division (towards negative infinity) and Euclidean remainder (same sign as divisor), whereas the latter follows the truncating division (toward 0) and truncated remainder (same sign as dividend). therefore, we need to be careful when implementing the solution for this problem.

# cf.) in the beginning, i solved like this: https://leetcode.com/problems/reverse-integer/submissions/2060805027/. however, it's technically wrong because it doens't follow the overflow constraints. i realized that after submitting this code, and noticed that i could simply check the overflow condition before doing `ans = ans*10 + r`. thus, i modified the code like below. btw, python's solution in the Editorial section is also incorrect due to the same reason.

# cf.) we can mimic the python's division and modulo behavior like other languages (C++, Golang, etc.), and implement the solution like this: https://leetcode.com/problems/reverse-integer/submissions/2060906622/—runtime: 48 ms (beats 43.38%), memory: 19.19 MB (beats 68.69%)


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        is_negative = x < 0
        x_abs = abs(x)
        ans = 0

        while x_abs > 0:
            x_abs, r = divmod(x_abs, 10)
            pos_overflow = ans > (INT_MAX - r) / 10
            neg_overflow = ans > (-INT_MIN - r) / 10
            if (not is_negative and pos_overflow) or (is_negative and neg_overflow):
                return 0

            ans = ans*10 + r

        return -ans if is_negative else ans


# notes while solving:
# ans * 10 + r > 2 ** 31 - 1 ? 
# ans > (2**31 - 1 - r) / 10

# - (ans*10 + r) < -2**31
# ans*10 + r > -INT_MIN
# ans > (-INT_MIN - r) / 10

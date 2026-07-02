# submission: https://leetcode.com/problems/powx-n/submissions/1704096280/
# runtime: 1 ms (beats 32.17%), memory: 17.65 MB (beats 100.00%)
# 27 min
# solved using divide-and-conquer / binary exponentiation (iterative approach)


# TC: O((log |n|)^2), where n is the exponent 'n' in the functim myPow(...).
# SC: O(1)


# From LeetCode Top Interview 150 - Math

# at first, i tried with a brute force approach, where you simply multiply x by itself n times and consider the sign of n. of course, however, this is not what the problem expects. after noticing that the range of n is from - (2 ** 31) to 2 ** 31 - 1, i realized that the brute force approach may raise the time limit exceeded error. so, i tried finding a test case that would cause this error, which was x = 1.000000001 and n = 2147483647 (2 ** 31 - 1).

# then, while attempting with the brute force (linear time) approach, i found out that i could approximately compute the answer by doubling the 'x' value for 'k' times until k meets the condition 2 ** k <= n <= 2 ** (k + 1). with this chain of thought, i realized that the 'n' can be represented as 2 ** a + 2 ** b + ... + 2 ** z, which is simply the binary representation of 'n', where a, b, ..., z are the indices of the bits that are set to 1 in 32 bit integer.

# therefore, i can utilize binary representation of 'n' to compute the answer in logarithmic time.


# cf.) the standard (or better) iterative binary exponentation solution performs in O(log |n|) time. this solution takes O((log |n|)^2) time since it recomputes the squaring results instead of reusing them. standard iterative solution can be found in the README.md.

# cf.) below is the iterative solution using python's built-in bin() function. "07_19_2025_recursive.py" contains the recursive solution.


class Solution:
    def myPow(self, x: float, n: int) -> float:
        n_abs = abs(n)
        n_bin_r = list(reversed(bin(n_abs)[2:]))

        ans = 1
        for i, digit_bin in enumerate(n_bin_r):
            if digit_bin == '1':
                factor = x
                for _ in range(i):
                    factor *= factor

                ans *= factor

        return ans if n > 0 else 1 / ans

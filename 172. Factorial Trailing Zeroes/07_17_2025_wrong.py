# problem: https://leetcode.com/problems/factorial-trailing-zeroes/

# 50 min

# From LeetCode Top Interview 150 - Math

# spent 50 min to solve the problem but could not. below is my attempt.

# i kept the number of trailing zeroes in `ans` and the last 't' digits of the current factorial excluding trailing zeros in `trailing_num`. Here, 't' is the number of digits in the next number to be multiplied. i am not sure why i assummed keeping the last 't' digits would be enough (and work) to compute the trailing zeroes. (no reasoning supported..)

# refer to the Editorial section for the correct approach and the solution for the follow-up question. (got shocked again)


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        trailing_num = 1

        for k in range(2, n + 1):
            trailing_num *= k

            while trailing_num % 10 == 0:
                ans += 1
                trailing_num = trailing_num // 10

            num_digits = len(str(k + 1))
            divisor = 10 * num_digits

            trailing_num %= divisor

        return ans

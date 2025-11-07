# submission: https://leetcode.com/problems/factorial-trailing-zeroes/submissions/1823467721/
# runtime: 11 ms, memory: 17.86 MB

# 19 min
# TC: O(n), where n is the input number.
# - for base 5, the inner loop runs n // 5 times (number of multiples of 5 up to n)
# - for base 25, the inner loop runs n // 25 times (number of multiples of 25 up to n)
# - ...
# - for base 5^k, the inner loop runs n // 5^k times (number of multiples of 5^k up to n)
# - therefore, the total number of iterations T(n) is n // 5 + n // 25 + ... + n // 5^k = n * \frac{1/5}{1 - 1/5} = n/4
# - and we know clearly that n/5 <= T(n) <= n/4, which menas T(n) is O(n) (more formally omega(n)).
# SC: O(1)


# the key idea is to count the number of multiples of 5, 25, 125, ..., up to n. the reasoning is that to count the number of trailing zeros, we need to count the number of factor 10s in the n!. each factor 10 is composed of a factor 2 and a factor 5, and we clearly know that the number of factor 2s is always greater than or equal to the number of factor 5s. therefore, we only need to count the number of factor 5s.

# the below code exactly implements the above idea by couting the factor 5 one by one. however, we can further optimize this by noticing that the number of multiples of 5, 25, 125, ..., up to n is actually the number of multiples of 5^k up to n. therefore, we can use a single loop to count the number of multiples of 5^k up to n, leading the time complexity to O(log_5(n)). for the optimized code, refer to the markdown file. this optimized version is the solution for the follow-up question.

# cf.) the code below's logic is identical to the Editorial's Approach 2, and the optimized version's logic would be the same as the Editorial's Approach 3.


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        base = base_mul = 5
        while base <= n:
            while base_mul <= n:
                ans += 1
                base_mul += base

            base *= 5
            base_mul = base

        return ans

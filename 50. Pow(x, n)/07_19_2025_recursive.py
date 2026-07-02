# submission: https://leetcode.com/problems/powx-n/submissions/1704089575/
# runtime: 0 ms (beats 100.00%), memory: 17.69 MB (beats 100.00%)
# 43 min (time includes solving "07_19_2025.py")
# solved using divide-and-conquer / binary exponentiation (recursive approach)
# saw the "recursion" tag in the topics

# TC: O(log |n|), where n is the exponent 'n' in the functim myPow(...).
# SC: O(log |n|), for the recursion stack space.


# From LeetCode Top Interview 150 - Math

# Below is a recursive solution that i implemented after noticing that the topics also contain the "Recursion" tag.


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def bin_pow(x, n):
            if n == 0: return 1
            if n < 0: return 1 / bin_pow(x, -n)

            return (x if n % 2 == 1 else 1) * bin_pow(x * x, n // 2)

        return bin_pow(x, n)

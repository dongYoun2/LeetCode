# submission: https://leetcode.com/problems/powx-n/submissions/1704089575/?envType=study-plan-v2&envId=top-interview-150
# runtime: 0 ms, memory: 17.7 MB

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

# submission: https://leetcode.com/problems/reverse-bits/submissions/1822810132/
# runtime: 35 ms, memory: 17.85 MB

# 5 min
# TC: O(1), since the number of bits is fixed at 32.
# SC: O(1)


# this solution actually has potential bugs. note that the number of iterations is 31, not 32. the submission passes because `n` is at most 2^31 - 2, where MSB is always 0, which in our case doesn't affect the result. however, if `n` becomes larger than 2^31 - 2, the code fails.

# the 06_26_2025.py is a more robust and correct solution.


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        last_bit_mask = 1
        for _ in range(31):
            ans |= n & last_bit_mask
            ans <<= 1
            n >>= 1

        return ans

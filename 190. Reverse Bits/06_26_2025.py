# submission: https://leetcode.com/problems/reverse-bits/submissions/1677787515/
# rutime: 42 ms, memory: 18 MB

# 7 min
# TC: O(1), the number of bits is fixed at 32.
# SC: O(1)


# From LeetCode Top Interview 150 - Bit Manipulation

# Performing bit operation digit by digit.


class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0

        for _ in range(32):
            last_bit = n & 1
            n >>= 1
            output <<= 1
            output |= last_bit

        return output

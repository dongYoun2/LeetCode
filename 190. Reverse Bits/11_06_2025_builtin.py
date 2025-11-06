# submission: https://leetcode.com/problems/reverse-bits/submissions/1822807194/
# runtime: 33 ms, memory: 17.79 MB

# 6 min
# TC: O(1), since the number of bits is fixed at 32.
# SC: O(32) -> O(1)


# solution with using python's built-in functions, including `bin(...)` and `zfill(...)`.


class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:].zfill(32)[::-1]
        return int(x, 2)

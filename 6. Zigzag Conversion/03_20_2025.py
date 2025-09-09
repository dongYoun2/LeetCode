# https://leetcode.com/problems/zigzag-conversion/description/

# took 40 min
# n: input string length
# TC: O(n)
# SC: O(1) (output space not considered)
# Although a nested loop is used, the time complexity is O(n).

# Felt like a simulation problem (but the approach below is actually arithmetic approach based on the index-based calculation). I think finding the pattern is the core of this problem.

# At first, I thought all rows had the same offset. However, due to the nature of the zigzag pattern, each row has different offsets, and they alternate within the row except for the first and last rows.


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        output = ""
        periodic = (numRows - 1) * 2

        for i in range(numRows):
            curr = i
            offset = i * 2

            while True:
                output += s[curr]
                offset = periodic - offset
                if offset == 0: # to handle the first and last row's indicies (skip duplicate index)
                    offset = periodic - offset
                curr += offset
                if curr >= len(s):
                    break

        return output


# Notes while solving the problem

# numRows = 5
# P0        H8
# A1     S7 I9
# Y2   I6   R10
# P3 L5     I11  G13
# A4        N12

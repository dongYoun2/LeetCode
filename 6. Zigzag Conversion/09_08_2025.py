# submission: https://leetcode.com/problems/zigzag-conversion/submissions/1764128439/
# runtime: 320 ms, memory: 24.6 MB

# 32 min
# TC: O(n * numRows), where n is the length of the input string
# SC: O(n * numRows) for the 2D matrix


# at first, i tried to solving the mathematical pattern, which i rememeber that i solved in this way on the very first attempt of this problem (03_20_2025.py). however, it took longer than i expected, so i switched to tryi simulating the zigzag, which i haven't tried solving in this way before.

# i defined the 2D matrix of size (numRows * len(s)) initiallized with empty strings (but it turns out that for optimal solution for the simulation approach, i didn't need to fill in with empty strings, as shown in the README file). then, i filled in the characters in the zigzag pattern by moving down and up-right in a loop until all characters are placed.

# variables are as follows:
# i: to track the index of the input string
# x and y: used to track the current position in the 2D matrix
# cnt: to count the number of rows filled in the current direction (down or up-right)

# for the optimized code for the simulation approach, refer to the README file.


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        mat = [[''] * len(s) for _ in range(numRows)]
        mat[0][0] = s[0]

        y = x = 0
        i = 1
        while i < len(s):
            cnt = 1
            while cnt < numRows and i < len(s):    # down
                y += 1
                mat[y][x] = s[i]

                i += 1
                cnt += 1

            cnt = 1
            while cnt < numRows and i < len(s):    # up-right
                y -= 1
                x += 1
                mat[y][x] = s[i]

                i += 1
                cnt += 1

        ans = [c for row in mat for c in row if c != '']
        return ''.join(ans)

# submission: https://leetcode.com/problems/zigzag-conversion/submissions/1764178638/
# runtime: 15 ms, memory: 18 MB

# 29 min
# TC: O(n), where n is the length of the input string
# SC: O(n) (`ans` list)


# after solving with the simulation approach (09_08_2025.py), i revisited the mathematical pattern (index computation) approach to optimize further. after analyzing several cases (numrRows = 2, 3, 4, 5), i was able to derive the pattern. it actually took shorter than the first time (03_20_2025.py), but the code itself seems to be simpler before.

# for more readable code, refer to the README file.


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = []
        for i in range(numRows):
            j = i
            if j == 0 or j == numRows - 1:  # first or last row
                while j < len(s):
                    ans.append(s[j])
                    j += (numRows - 1) * 2
            else:
                total_hop = (numRows - 1) * 2
                second_hop = 2 * i
                first_hop = total_hop - second_hop
                flag = 0

                while j < len(s):
                    ans.append(s[j])
                    j += first_hop if flag % 2 == 0 else second_hop
                    flag += 1

        return "".join(ans)

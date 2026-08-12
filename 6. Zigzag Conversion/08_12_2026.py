# submission: https://leetcode.com/problems/zigzag-conversion/submissions/2104584381/
# runtime: 2 ms (beats 99.05%), memory: 19.37 MB (beats 45.91%)
# 27 min
# solved using the mathematical pattern approach (same logic as the README.md's "Mathematical Approach (computing indices)" section)

# refer to the README.md's "Mathematical Approach" for a complexity analysis


# took a little longer than expected, but seems it's alright. more readable variable naming would be better. refer to the README.md's "Mathematical Approach" for a better code.


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = []
        full_cycle = 2*(numRows-1)
        for i in range(numRows):
            cycle = 2*i
            j = i
            while j < len(s):
                ans.append(s[j])

                cycle = full_cycle - cycle
                if cycle == 0:
                    cycle = full_cycle - cycle

                j += cycle

        return ''.join(ans)

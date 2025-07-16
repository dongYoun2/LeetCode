# submission: https://leetcode.com/problems/number-of-1-bits/submissions/1700365295/
# runtime: 0 ms, memory: 17.7 MB

# 1 min
# TC: O(1)
# SC: O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        n_binary = bin(n)

        return sum(1 for c in n_binary if c == '1')

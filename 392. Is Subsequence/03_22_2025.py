# https://leetcode.com/problems/is-subsequence/

# took 4 min
# TC: O(|t|), where |t| is the length of 't'
# SC: O(1)

# This can be seen as the two-pointer algorithm, where each pointer is 'pos' and 'c'.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        pos = 0
        for c in t:
            if s[pos] == c:
                pos += 1

            if pos >= len(s):
                return True

        return False

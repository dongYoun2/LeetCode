# submission: https://leetcode.com/problems/is-subsequence/submissions/1787305905/
# runtime: 0 ms, memory: 71.76 MB

# 7 min
# TC: O(|t|), where |t| is the length of t
# SC: O(1)

# the main idea for this solution is using two pointers and greedily checking if the characters in s are in t in order.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if len_s == 0:
            return True
        elif len_t == 0:
            return False

        pos = 0
        for i in range(len_t):
            if t[i] == s[pos]:
                pos += 1
                if pos >= len_s:
                    return True

        return False

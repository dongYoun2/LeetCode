# problem: https://leetcode.com/problems/ransom-note/
# submission: https://leetcode.com/problems/ransom-note/submissions/1597824846/

# 4 min
# TC: O(n + m), where n is the length of ransomNote and m is the length of magazine
# SC: O(n + m)

# Without using Counter; with only pure dictionary

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_cntr = {}

        for c in magazine:
            mag_cntr[c] = mag_cntr.get(c, 0) + 1

        for c in ransomNote:
            if c not in mag_cntr or mag_cntr[c] <= 0:
                return False
            mag_cntr[c] -= 1

        return True

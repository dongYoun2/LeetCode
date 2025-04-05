# problem: https://leetcode.com/problems/ransom-note/
# submission: https://leetcode.com/problems/ransom-note/submissions/1597822336/

# 4 min
# TC: O(n + m), where n is the length of ransomNote and m is the length of magazine
# SC: O(n + m)

# Knew that it's a hashamp problem; I used  python Counter.

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_cntr = Counter(ransomNote)
        mag_cntr = Counter(magazine)

        diff = ransom_cntr - mag_cntr

        return len(diff) == 0

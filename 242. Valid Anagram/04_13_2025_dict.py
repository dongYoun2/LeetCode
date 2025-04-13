# problem: https://leetcode.com/problems/valid-anagram/
# submission: https://leetcode.com/problems/valid-anagram/submissions/1605747933/

# TC: O(|s| + |t| + 26) -> O(|s| + |t|), where 26 is the number of English lowercase letters (problem constraint)
# SC: O(26) -> O(1)

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_cntr = defaultdict(int)
        t_cntr = defaultdict(int)

        for c in s:
            s_cntr[c] += 1

        for c in t:
            t_cntr[c] += 1

        return s_cntr == t_cntr

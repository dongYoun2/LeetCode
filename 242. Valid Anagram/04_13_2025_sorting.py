# problem: https://leetcode.com/problems/valid-anagram/
# submission: https://leetcode.com/problems/valid-anagram/submissions/1605746471/

# TC: O(|s| log |s| + |t| log |t|)
# SC: O(|s| + |t|) (if sorting is done in-place, SC is O(1))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

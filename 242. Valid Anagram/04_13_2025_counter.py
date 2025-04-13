# problem: https://leetcode.com/problems/valid-anagram/
# submission: https://leetcode.com/problems/valid-anagram/submissions/1605745800/

# TC: O(|s| + |t| + 26) -> O(|s| + |t|), where 26 is the number of English lowercase letters (problem constraint)
# SC: O(26) -> O(1)


from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

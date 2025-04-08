# problem: https://leetcode.com/problems/isomorphic-strings/
# submission: https://leetcode.com/problems/isomorphic-strings/submissions/1600759773/

# 6 min
# TC: O(n), n is the length of the string (either s or t, since in the problem constraint, they are equal)
# SC: O(1), since the number of characters is limited to 128 for standard ASCII or 256 for extended ASCII

# From LeetCode Top Interview 150 - Hashmap

# At first, I used only one hash table to map characters from s to t, but it failed for cases like "ab" and "aa". Since we need one-to-one mapping for both strings, we need to use two hash tables to map characters from s to t and t to s. The idea is to check if the mapping is consistent for both strings.

# cf.) LeetCode Editorial's Approach 2: First occurence transformation also provides interesting index mapping idea.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_to_t, t_to_s = {}, {}
        for c_s, c_t in zip(s, t):
            if c_s in s_to_t:
                if s_to_t[c_s] != c_t:
                    return False

            if c_t in t_to_s:
                if t_to_s[c_t] != c_s:
                    return False

            s_to_t[c_s] = c_t
            t_to_s[c_t] = c_s

        return True

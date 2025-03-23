# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# took 1 min
# using python built-in function

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

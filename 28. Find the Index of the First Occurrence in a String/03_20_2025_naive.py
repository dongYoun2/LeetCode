# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# took 5 min
# n: length of text to search on
# m: length of string pattern
# TC: O(n*m)
# SC: O(1)

# This is a naive way to search string patterns. I know the KMP algorithm is more efficient since it has linear time complexity (O(n+m)). However, I forgot the concepts, so I will study the KMP algorithm at this chance.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if needle == haystack[i:i+m]:
                return i

        return -1

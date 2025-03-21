# https://leetcode.com/problems/valid-palindrome/description/

# 3 min
# TC: O(n) - three-pass.
# SC: O(n) - additional storage for reversed string.

# used python built-in function and slicing.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_s = "".join([c.lower() for c in s if c.isalnum()])

        return processed_s == processed_s[::-1]

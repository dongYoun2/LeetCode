# https://leetcode.com/problems/valid-palindrome/

# 9 min
# TC: O(n) - one-pass
# SC: O(1)

# using a two-pointer algorithm with one-pass. It's important to check bounds for pointers and "return True" when either of them is out of range because this means the input string only contains non-alphanumeric characters. (At first, I forgot to check that.)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1

            while r >= 0 and not s[r].isalnum():
                r -= 1

            if l >= len(s) or r < 0:
                break

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True
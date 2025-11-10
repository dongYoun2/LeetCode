# submission: https://leetcode.com/problems/longest-palindromic-substring/submissions/1826166016/
# runtime: 307 ms, memory: 17.94 MB

# 23 min
# time and space complexity are mentioned in the "08_04_2025_two_pointers.py" solution.


# expand from center approach.

# it took a little longer than i expected due to some debugging. i could simply use the nonlocal variables instead of returning left, right (and length) from the `palindrome_centered` function.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def palindrome_centered(i, j):
            l, r = i, j
            assert s[l] == s[r]
            while l - 1 >= 0 and r + 1 < n and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            return l, r, r - l + 1

        max_len = 1
        ans_i = ans_j = 0
        for i in range(n):  # checking palindrome with odd length
            a, b, len_ = palindrome_centered(i, i)
            if len_ > max_len:
                max_len = len_
                ans_i, ans_j = a, b

        for i in range(n-1):    # checking palindrome with even length
            if s[i] != s[i+1]:
                continue
            a, b, len_ = palindrome_centered(i, i + 1)
            if len_ > max_len:
                max_len = len_
                ans_i, ans_j = a, b

        return s[ans_i:ans_j+1]

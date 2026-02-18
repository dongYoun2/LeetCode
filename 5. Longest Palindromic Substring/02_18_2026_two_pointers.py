# submission: https://leetcode.com/problems/longest-palindromic-substring/submissions/1923630391/
# runtime: 224 ms (beats 85.99%), memory: 19.35 MB (beats 58.15%)
# 11 min

# refer to the markdown file for a complexity analysis.


# solved using a two-pointer algorithm, implementing the `expand_from_center(...)` function.


# cf.) note that time complexity is the same as the DP solution, but this approach is much faster in practice since most centers won't produce long palindromes.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        assert s

        n = len(s)
        ans = s[0]

        def expand_from_center(i, j) -> str:
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break
                
                i -= 1
                j += 1
            
            return s[i+1:j]

        # odd
        for i in range(n):
            cand = expand_from_center(i, i)
            if len(cand) > len(ans):
                ans = cand

        # even
        for i in range(0, n-1):
            cand = expand_from_center(i, i+1)
            if len(cand) > len(ans):
                ans = cand
        
        return ans

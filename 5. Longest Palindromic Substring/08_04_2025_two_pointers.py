# submission: https://leetcode.com/problems/longest-palindromic-substring/submissions/1723161756/
# runtime: 495 ms, memory: 18 MB

# TC: O(n^2), where n is the length of the string s.
# SC: O(1)


# after noticing that this problem can also be solved using two pointers technique (expand from center), i solved it with that approach. as long as i can find out that this problem can be solved with two pointers during the interview, i believe the implementation would be quite straightforward.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [0, 0]
        get_len = lambda i, j: j - i + 1


        def expand_from_center(i, j):
            l, r = i, j

            while l >= 0 and r < n and s[l] == s[r]:
                if get_len(l, r) > get_len(ans[0], ans[1]):
                    ans[0], ans[1] = l, r

                l -= 1
                r += 1


        # odd
        for i in range(n):
            expand_from_center(i, i)

        # even
        for i in range(n-1):
            expand_from_center(i, i+1)

        return s[ans[0]:ans[1]+1]

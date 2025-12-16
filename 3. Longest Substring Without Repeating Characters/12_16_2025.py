# submission: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1857553904/
# runtime: 35 ms, memory: 18.1 MB

# 14 min

# technically, fifth time solving this problem since 04/10/2024. instinctively noticed that i might have to use the sliding window technique. after a few simulations, i started to implement the code.

# but got wrong on a first submission since i missed to remove the leftmost character from the `seen`set while shrinking the window lol.

# another thing i searched up again is the difference between the `remove()` and `discard()` of the set.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        ans = 0
        l = 0
        for r in range(n):
            if s[r] not in seen:
                ans = max(ans, r - l + 1)
                seen.add(s[r])
                continue

            while s[l] != s[r]:
                seen.remove(s[l])
                l += 1
            l += 1

        return ans

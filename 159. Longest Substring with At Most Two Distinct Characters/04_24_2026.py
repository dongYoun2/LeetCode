# submission: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/submissions/1987203398/
# runtime: 190 ms (beats 35.18%), memory: 19.71 MB (beats 37.68%)
# 8 min
# solved with the sliding window technique

# TC: O(2n) -> O(n)
# SC: O(1) (at most 2 distinct characters in a hash table)


# chose from a neetcode "sliding window" category.

# knew this is a sliding window problem. pretty straightforward solution.


from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        seen = defaultdict(int)
        ans = left = 0
        for right in range(n):
            seen[s[right]] += 1
            while len(seen) > 2:
                seen[s[left]] -=1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                
                left += 1
            ans = max(ans, right-left+1)

        return ans

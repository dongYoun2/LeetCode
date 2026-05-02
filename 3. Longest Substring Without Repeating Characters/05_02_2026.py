# submission: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1993607665/
# runtime: 15 ms (beats 42.81%), memory: 19.42 MB (beats 7.75%)
# 8 min
# solved with a (variable-sized) sliding window technique


# chose from a neetcode "sliding window" category.

# after failing to solve the "424. Longest Repeating Character Replacement" today, i attempted this problem. both uses a similar idea, but this problem is a little easier as we can directly use the hash table (set) to check the condition in a true O(1) time.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        left = ans = 0
        for right in range(n):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            
            seen.add(s[right])
            ans = max(ans, right-left+1)

        return ans

# problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# submission: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1588646885/

# 13 min
# TC: O(n^2) (This is because the membership check on the python slice is O(n). We can optimize this to O(1) by using a hash table (set or dictionary))
# SC: O(n) (due to the python slice)

# I solved this question previously on 11/28/2024. Interestingly, I used "set" for the membership check then. Also, I solved this problem knowing that I had to use the 'sliding window' technique beforehand, as I am currently solving problems based on the algorithm type.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = r = 0
        max_len = 1
        while True:
            r += 1
            if r >= len(s):
                break

            while s[r] in s[l:r]:
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len

# notes while solving this problem:
# a a b
# submission: https://leetcode.com/problems/permutation-in-string/submissions/2012067934/
# runtime: 23 ms (beats 48.28%), memory: 19.53 MB (beats 19.21%)
# 50 min
# solved with a (variable-size) sliding window technique; optimal in terms of time complexity

# symbols:
# - m: length of s1
# - n: length of s2

# TC: O(2*n) -> O(n) (each left and right pointer iterates at most n times)
# SC: O(26) -> O(1) (bounded by the number of lowercase English letters)


# chose from a neetcode "sliding window" category.

# directly approached with a "variable-size" sliding window technique. was trickier handling the `else` block, which contains a while loop to shrink the window; moving the left pointer forward (two wrong sumbissions because of this). also spent a bit of time debugging this part.

# there are other solutions with a "fixed-size" sliding window technique as well as using sorting. refer to the README.md for more details.


from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cntr = Counter(s1)
        left = 0
        for right in range(len(s2)):
            if cntr[s2[right]] > 0:
                cntr[s2[right]] -= 1
                if cntr[s2[right]] == 0:
                    del cntr[s2[right]]
                if not cntr:
                    return True
            else:
                while s2[left] != s2[right]:
                    cntr[s2[left]] += 1
                    left += 1
                left += 1

        return False

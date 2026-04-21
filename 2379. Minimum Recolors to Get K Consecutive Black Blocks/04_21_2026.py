# submission: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/submissions/1984428606/
# runtime: 0 ms (beats 100.00%), memory: 19.26 MB (beats 67.70%)
# 13 min

# TC: O(n)
# SC: O(1) (temporary space for a slice is not considered)


# chose from a neetcode "sliding window" category.

# directly approached with the sliding window technique. spent a bit of time for debugging cause i used 'w' (the lowercase letter) instead of 'W' (the uppercase letter) lol.


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = curr_w = sum(e == 'W' for e in blocks[:k])
        for i in range(k, n):
            curr_w += - int(blocks[i-k] == 'W') + int(blocks[i] == 'W')
            ans = min(ans, curr_w)
        
        return ans

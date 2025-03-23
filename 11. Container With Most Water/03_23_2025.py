# https://leetcode.com/problems/container-with-most-water/

# 15 min
# TC: O(n)
# SC: O(1)

# I misunderstood the question statement at first. I thought the two "endpoints" meant the two bars, one at index `i` (itself) and the other at index `height[i]` for each index `i`. So I just scanned through the `height` in one pass, comparing the current area at index `i` with the maximum area that has been found so far.

# However, this is not what the question asked for lol. Basically, what the question meant is the maximum area that could be formed with any two bars. We can choose any two bars from the `height` array.

# This can be solved using two pointers, one moving forward from the front, and the other moving backward from the rear while keep tracking the maximum area.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            if height[l] < height[r]:
                max_area = max(max_area, (r-l)*height[l])
                l += 1
            else:
                max_area = max(max_area, (r-l)*height[r])
                r -= 1

        return max_area

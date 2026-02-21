# submission: https://leetcode.com/problems/container-with-most-water/submissions/1926628015/
# runtime: 46 ms (beats 93.11%), memory: 29.62 MB (beats 50.42%)
# 13 min

# refer to the 03_23_2025.py for the complexity analysis.


# i solved using two-pointer approach. pretty straightforward question.

# cf.) one thing to note is that in my implementation i moved both left and right pointers when the heights are the same. this seems to be a little faster in practice. however, it's also totally fine to move either one when they are same (submision link for this implementation: https://leetcode.com/problems/container-with-most-water/submissions/1926634191/, and 03_23_2025.py implements in that way too).


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1

        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
            
        return ans

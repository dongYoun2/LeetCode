# submission: https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/2020505672/
# time limit exceeded (TLE)


# TC: O(n log n + n^2) -> O(n^2)
# SC: O(n) (sorting)

# chose from a neetcode "sliding window" category.

# below is the very first solution i came up with. as mentioned above, i knew i had to use a sliding window technique (tbh, i don't think i could solve this problem if i had no clue which algorithm to use).

# `diff` computation logic takes linear time and thus the overall loop takes n^2 time. since the input size is up to 10^5, i expected this solution to be TLE. i tried to optimize this per-window computation (`diff` computation), and solved it in "06_02_2026.py".


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 1
        left = 0
        for right in range(1, n):
            diff = 0
            for i in range(left, right):
                diff += nums[right] - nums[i]
            
            if diff <= k:
                ans = max(ans, right-left+1)
            else:
                left += 1
        
        return ans

# notes while solving:
# expected TC: n log n + n^2 ?

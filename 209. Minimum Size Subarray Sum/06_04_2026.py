# submission: https://leetcode.com/problems/minimum-size-subarray-sum/submissions/2022663179/
# runtime: 6 ms (beats 96.97%), memory: 30.72 MB (beats 16.06%)
# 15 min
# solved with a sliding window technique

# TC: O(n), where n is the length of nums
# SC: O(1)


# chose from a neetcode "sliding window" category.

# below is a straightforward solution. this is exactly the same as the implementation in the README's "Sliding Window" section. in the beginning, i thought we are looking for the smallest subarray where the sum is "exactly equal" to target. so i wrote the code for that, which results in a wrong submission (https://leetcode.com/problems/minimum-size-subarray-sum/submissions/2022661780/) lol, but after noticing that, i could solve it with a small change. 


import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = math.inf

        left = 0
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            
        return 0 if ans == math.inf else ans
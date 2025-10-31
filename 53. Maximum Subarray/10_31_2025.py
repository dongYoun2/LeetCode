# submission: https://leetcode.com/problems/maximum-subarray/submissions/1816994573/
# runtime: 90 ms, memory: 32.14 MB

# 8 min
# TC: O(n), where n is the length of nums
# SC: O(1)


# this is a Kadane's algorithm solution (i have forgotten that the below code is actually a Kadane's algorithm lol). howeveer, i didn't think of it's a (greedy) dynamic programming approach. rather, i thought it's a solely greedy solution.

# cf.) now it's good to remeber that the Kadane's algorithm solves the maximum subarray sum problem in O(n) time and O(1) space.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert nums
        ans = curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(0, curr_sum)
            curr_sum += nums[i]
            ans = max(ans, curr_sum)

        return ans

# notes while solving:
# negative, positive numbers
# always good to add pos number

# greedy? O(n)

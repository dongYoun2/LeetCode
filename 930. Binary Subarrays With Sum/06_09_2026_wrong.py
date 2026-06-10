# 35 min
# wrong solution


# chose from a neetcode "sliding window" category.

# this is the first solution i coded, but it fails on my added test case: nums = [1,0,1,0,0,0], goal = 1.

# i directly approached with the sliding window technique since i chose from the "sliding window" category. i was assured that i need to apply a standard variable size sliding window pattern, but based on the second test case, i noticedd that this pattern can not be applied when the `goal` is 0. so i handled as a special case, mathematically computing the answer.

# however, a critical issue is that including zeros doesn't change the current sum. therefore, we may miss some correct subarrays with leading zeros. For example, in the above failed test case, the solution below misses three correct subarrays: [0, 1, 0], [0, 1, 0, 0], and [0, 1, 0, 0, 0].


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        if goal == 0:
            zeros = 0
            for n in nums:
                if n == 0:
                    zeros += 1
                elif zeros != 0:
                    ans += zeros * (zeros+1) // 2
                    zeros = 0
            
            if zeros > 0:   # process the remaining zeros subarray
                ans += zeros * (zeros+1) // 2
        
        else:
            l = curr_sum = 0
            for r in range(len(nums)):
                curr_sum += nums[r]
                if curr_sum == goal:
                    ans += 1
                elif curr_sum > goal:

                    while curr_sum >= goal and l < r:
                        curr_sum -= nums[l]
                        l += 1
                        if curr_sum == goal:
                            ans += 1

        return ans

# 50 min (time including writing the "06_09_2026_wrong.py" solution)
# Time Limit Exceeded

# TC: O(n^2)
# SC: O(1)


# the logic itself is correct, but the time complexity is quadratic. a pure brute force solution would be O(n^3), so this would be a naive solution with a simple sliding window optimization for running sum.

# goal == 0 is still handled as a special case just like in the "06_09_2026_wrong.py" solution.

# what i basically did is that for each possible subarray size (window size), i computed the running sum of the subarray, and checked if it matches the target `goal`. if it does, i increment the answer. so this requires the nested loop, which makes the n^2 time complexity.

# cf.) assumed this would raise TLE, but just tried.


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
            for sz in range(goal, len(nums)+1):
                ones = sum(nums[:sz])
                if ones == goal: 
                    ans += 1 
                for i in range(sz, len(nums)):
                    ones = ones - nums[i-sz] + nums[i]
                    if ones == goal:
                        ans += 1
        
        return ans

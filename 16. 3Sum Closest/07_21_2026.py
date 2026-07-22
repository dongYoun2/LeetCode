# submission: https://leetcode.com/problems/3sum-closest/submissions/2076278815/
# runtime: 345 ms (beats 83.89%), memory: 19.50 MB (beats 15.23%)
# 15 min
# solved with two pointers

# TC: O(n^2)
# SC: O(1)


# this is a variant of the 3Sum problem. the difference is that we don't need any optimization for the two pointers in this problem. one minor improvement would be iterating until n - 2 for the outer loop since we need 3 numbers at the distinct indices.


import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans_diff = math.inf

        for i in range(n):
            l, r = i + 1, n - 1

            while l < r:
                goal = nums[i] + nums[l] + nums[r]
                diff = goal - target

                if diff == 0:
                    return target

                if abs(diff) < abs(ans_diff):
                    ans_diff = diff
                
                if diff > 0:
                    r -= 1
                else:
                    l += 1

        return target + ans_diff

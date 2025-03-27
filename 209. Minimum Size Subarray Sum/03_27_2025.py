# problem: https://leetcode.com/problems/minimum-size-subarray-sum/
# submission: https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1588557086/

# 12 min
# TC: O(n)
# SC: O(1)

# I solved this problem, knowing which algorithm to use beforehand since I chose the problem from the "sliding window" category. With knowing which algorithm to use, it wasn't that difficult. But I believe it is more important to attempt without knowing the algorithm, so I will try it after solving problem category by category to get a solid grasp of each type.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        min_len = len(nums) + 1
        curr_sum = nums[0]

        while True:
            if curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1
            else:
                r += 1
                if r >= len(nums):
                    break

                curr_sum += nums[r]

        return min_len if min_len < len(nums) + 1 else 0

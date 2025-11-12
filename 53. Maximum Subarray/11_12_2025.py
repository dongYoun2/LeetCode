# submission: https://leetcode.com/problems/maximum-subarray/submissions/1827927543/
# runtime: 89 ms, memory: 32.88 MB

# 3 min
# complexity analysis is mentioned in the "06_02_2025.py" solution.


# typical solution for the maximum subarray problem is to use Kadane's algorithm.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's alg.
        assert nums
        n = len(nums)
        ans = curr = nums[0]
        for i in range(1, n):
            curr = max(0, curr) + nums[i]
            ans = max(ans, curr)

        return ans

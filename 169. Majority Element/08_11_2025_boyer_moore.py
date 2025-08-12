# submission: https://leetcode.com/problems/majority-element/submissions/1731851650/
# runtime: 4 ms, memory: 19.4 MB


# 7 min
# TC: O(n)
# SC: O(1)


# From LeetCode Top Interview 150 - Array / String

# after solving with a sorting approach (08_11_2025.py), i attempted to solve with Boyer-Moore Voting Algorithm, and could successfully implement it.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        cnt = 1

        for i in range(1, len(nums)):
            if ans == nums[i]:
                cnt += 1
            elif cnt <= 0:
                cnt += 1
                ans = nums[i]
            else:
                cnt -= 1

        return ans

# notes while solving:
# 1 1 2 2 2 1 1

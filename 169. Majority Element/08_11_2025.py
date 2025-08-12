# submission: https://leetcode.com/problems/majority-element/submissions/1731845853/
# runtime: 4 ms, memory: 19.43 MB

# 1 min
# TC: O(n log n) due to sorting
# SC: O(1)


# From LeetCode Top Interview 150 - Array / String

# I have solved this problem several times before. This problem can also be solved using (default) dictionary or Boyer-Moore Voting Algorithm, but sorting came to my mind first, and indeed, it's the simplest solution.

# cf.) For other approaches, refer to the markdown file.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

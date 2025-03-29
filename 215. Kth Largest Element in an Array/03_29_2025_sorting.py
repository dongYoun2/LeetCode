# problem: https://leetcode.com/problems/kth-largest-element-in-an-array/
# submission: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1590378875/

# 2 min
# TC: O(n log n)
# SC: O(n) (Python internally uses Timsort + immutable reversed)

# Solved using sorting.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[::-1][k-1]
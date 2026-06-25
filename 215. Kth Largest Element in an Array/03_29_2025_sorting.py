# submission: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1590378875/
# runtime: 51 ms (beats 85.57%), memory: 28.78 MB (beats 99.70%)
# 2 min
# solved using sorting

# TC: O(n log n)
# SC: O(n) (Python internally uses Timsort + immutable reversed)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[::-1][k-1]

# submission: https://leetcode.com/problems/squares-of-a-sorted-array/submissions/1786550895/
# runtime: 10 ms, memory: 19.37 MB
# this solution solves the follow-up question.

# 5 min
# TC: O(n), where n is the length of `nums`.
# SC: O(1), since the output array is not considered.


# The code  below solves the follow-up question. the key is to use two pointers to traverse the array from both ends.


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l, r = 0, len(nums) - 1

        while l <= r:
            a, b = nums[l] ** 2, nums[r] ** 2
            if a >= b:
                ans.append(a)
                l += 1
            else:
                ans.append(b)
                r -= 1

        ans.reverse()
        return ans

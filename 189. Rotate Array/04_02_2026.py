# submission: https://leetcode.com/problems/rotate-array/submissions/1966803585/
# runtime: 4 ms ( beats 66.57%), memory: 26.49 MB ( beats 80.43%)
# 3 min

# TC: O(n), where n is the length of the input array
# SC: O(n) (due to the temporary storage of the list slice)


# first time solved: 03/25/2024
# second time solved: 03/07/2025

# this is a third time solving this problem. i remeber that this problem can be solved by reversing the array three times. to make it truly O(1) space (follow-up question), we can simply define our own reverse function and use it. for that, refer to the Editorial's Approach 4 or this submission: https://leetcode.com/problems/rotate-array/submissions/1566403639/ 


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

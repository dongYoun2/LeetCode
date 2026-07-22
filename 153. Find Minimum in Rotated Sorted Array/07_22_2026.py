# submission: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/2077636849/
# runtime: 0 ms (beats 100.00%), memory: 19.43 MB (beats 24.34%)
# 16 min
# algorithm and the complexity analysis are the same as the "06_14_2025.py" solution. 


# directly spotted this problem is a binary search problem. we can easily notice that with the O(log n) time requirement as well. the key is to compare the middle element with the rightmost element since the `nums[r]` is always the largest element in the right sorted portion.

# - if nums[m] < nums[r], the mid element is in the right (smaller) portion, so the minimum resides in the left (larger) portion.
# - if nums[m] > nums[r], the mid element is in the left (larger) portion, so the minimum must be in the right (smaller) portion.

# cf.) in the code below, it's safer with `if m > 0 and nums[m-1] > nums[m]` instead of `if nums[m-1] > nums[m]` since m-1 becomes -1, where nums[-1] represents the last element of the array in Python when m is 0. however, since we perform early return with `if nums[0] < nums[-1]:`, which checks whether the first element is the minimum, we don't need to worry about this issue here.

# cf.) instead of these two early returns below, we can make the algorithm more general and concise. refer to here for the submission: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/2077648771/.


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        n = len(nums)
        l, r = 0, n-1
        
        while l < r:
            m = l + (r - l) // 2

            if nums[m-1] > nums[m]:
                return nums[m]
            
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1

        return nums[l]


# notes while solving:
# 6 7 0 1 2 4 5

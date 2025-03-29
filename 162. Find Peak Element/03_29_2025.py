# problem: https://leetcode.com/problems/find-peak-element/
# submission: https://leetcode.com/problems/find-peak-element/submissions/1590242270/

# 21 min
# TC: O(log n)
# SC: O(1)

# I used binary search to solve this problem, but I knew that I had to use binary search as I am currently solving problems based on the algorithm type. Although I knew which algorithm to use beforehand, it was a bit tricky to figure out how to use it. Specifically, it took me a while to find out which subarray (left or right) to search after running a binary search. That is, I wasn't sure how to determine which side guarantees that there is a peak element. I believe it is important to notice from the constraint nums[i] != nums[i + 1] that there is always a peak element in the input array. Also, simulating on the ascending or descending array helped me digest the problem better.

# The below code contains a lot of if-else statements. This can be improved by 1) considering more edge cases in addition to the array with a single element or 2) using the `l < r` condition for the while loop instead of `l <= r`. For more details, refer to the markdown file and the LeetCode Editorial.

# cf.) This problem encouraged me to break the streotype that I can only use binary search when the array is sorted. I realized that I can also use it when the array is not sorted, as long as I can find a way to narrow down the search space. For example, in this case, I was able to narrow down the search space by checking if the middle element is greater than its neighbors. This is a good reminder that binary search can be applied in various situations, not just when the array is sorted.


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2 # prevent overflow

            if m == 0:
                if nums[m] > nums[m+1]:
                    return m
                else:
                    l = m + 1
            elif m == len(nums) - 1:
                if nums[m] > nums[m-1]:
                    return m
                else:
                    r = m - 1
            elif nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return m
            elif nums[m-1] > nums[m]:
                r = m - 1
            elif nums[m+1] > nums[m]:
                l = m + 1


# notes while solving:
# 1 2 3 1
# 1 2 1 3 5 6 4 7 8
# peak 무조건 존재
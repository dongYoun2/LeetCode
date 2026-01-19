# submission: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1889077468/
# runtime: 0 ms, memory: 19.53 MB

# 29 min
# time and space complexity is the same as in the README.md.


# took longer than expected. i was randomly thinking how to determine where the `target` is located. however, the key is that by checking which half is sorted (or the pivot is in which half), we can easily determine the location of the `target`.

# also, it's important to taking into account where the equality is needed when doing inequality checks on the `if` conditions. my first submission (https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1889075745/) failed because i missed the equality.

# to prevent this, it's good to always have a habit of thinking about the edge cases, such as where the number of elements is 1 or 2.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[m] < nums[r]:   # pivot is in left half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else: # pivot is in right half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1        

        return -1

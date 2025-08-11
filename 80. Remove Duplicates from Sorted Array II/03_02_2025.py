# Submission: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/1560993842/
# Runtime: 82 ms, Memory: 20.4 MB

# TC: O(n), where n is the length of the input array
# SC: O(1)


# From LeetCode Top Interview 150 - Array / String

# Approach below uses three pointers; current position (`i` in the loop), previous position (`prev`), and the previous to previous position (`prev_prev`). `pos` indicates the position to add the next unique element. The algorithm ensures that each element appears at most twice in the modified array.

# For more optimized approach, refer to the markdown file.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        pos = 2
        prev_prev = nums[0]
        prev = nums[1]

        for i in range(2, len(nums)):
            if prev != nums[i]:
                nums[pos] = nums[i]
                pos += 1
                prev_prev, prev = prev, nums[i]

            elif prev != prev_prev:
                nums[pos] = nums[i]
                pos += 1
                prev_prev = prev

        return pos

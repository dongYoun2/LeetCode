# submission: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/1726189336/
# runtime: 85 ms, memory: 20.4 MB

# 13 min
# TC: O(n), where n is the length of the input array
# SC: O(1), since we are modifying the input array in place


# From LeetCode Top Interview 150 - Array / String

# I solved this problem by tracking two variables:
# 1. `add_pos`: the position to add the next unique element
# 2. `freq`: the frequency of the current element
# This ensures that each element appears at most twice in the modified array.

# some code duplications can be avoided. For more details, refer to the markdown file.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        add_pos = 1
        freq = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if freq < 2:
                    nums[add_pos] = nums[i]
                    add_pos += 1

                freq += 1
            else:
                nums[add_pos] = nums[i]
                add_pos += 1
                freq = 1

        return add_pos

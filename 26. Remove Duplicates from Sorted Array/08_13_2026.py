# submission: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/2106011813/
# runtime: 0 ms (beats 100.99%), memory: 20.58 MB (beats 42.42%)
# 3 min
# solved with array manipulation (with two pointers)

# TC: O(n)
# SC: O(1)


# very straightforward; i keep track of the current index to write to and iterate through the array.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[curr] = nums[i]
                curr += 1

        return curr

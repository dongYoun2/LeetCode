# submission: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/2106020266/
# runtime: 81 ms (beats 84.69%), memory: 22.15 MB (beats 55.10%)
# 19 min (time includes writing "08_13_2026.py")
# array manipulation with two pointers (`prev` and `i`) and a counting variable

# TC: O(n)
# SC: O(1)


# i first compared the current value with the last value in the valid array (which is at index `prev`). if they are different, i reset the `cnt` variable to 1 and add the current value to the next index of the valid array. if they are the same and the `cnt` variable is less than 2, meaning one more duplicate is allowed, i increment the `cnt` variable, and inesert the current value just like the previous case. if the `cnt` variable is already 2, i simply skip the current value.

# however, however, instead of branching with wether the `cnt` is less than 2 or not, i can simply increment the `cnt` variable if the current value is the same as the last value in the valid array. then, when performing the main logic, which is inserting the current value to the next index of the valid array, i can simply guaurd it with `if cnt <= 2` condition. for more details and the implementation, refer to the README.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[prev]:
                cnt = 1
            elif cnt < 2:
                cnt += 1
            else:
                continue

            prev += 1
            nums[prev] = nums[i]

        return prev + 1

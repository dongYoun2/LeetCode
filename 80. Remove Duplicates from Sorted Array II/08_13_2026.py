# submission: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/2106020427/
# runtime: 77 ms (beats 94.00%), Memory: 22.45 MB (Beats 8.73%)
# solved with an array manipulation with two pointers (`prev` and `i`)
# 10 min

# TC: O(n)
# SC: O(1)


# for any number in a valid array, it can appear either once or twice. so i simply kept a boolean variable `twos` to keep track of that (instead of counting a real frequency). however, the code has some duplications. so after implementing like this, i coded up with a `cnt` variable which counts a frequency of the current number. the solution can be foind in "08_13_2026_cnt.py".


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        twos = False
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[prev]:
                prev += 1
                nums[prev] = nums[i]
                twos = False
            elif not twos:
                prev += 1
                nums[prev] = nums[i]
                twos = True

        return prev + 1

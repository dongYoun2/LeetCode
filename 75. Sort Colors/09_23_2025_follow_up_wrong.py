# submission: https://leetcode.com/problems/sort-colors/submissions/1780582778/
# wrong solution for the follow-up question

# 40 min

# i noticed that the idea is to push all 0s to the left and all 2s to the right. the idea is right, but failed to implement it correctly.

# the problem here is that when current element (nums[curr]) is 0, we also need to swap it with the element at zero_pos.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos, two_pos = 0, len(nums) - 1
        curr = 0

        while curr <= two_pos:
            if nums[curr] == 0:
                nums[zero_pos] = 0
                zero_pos += 1
            elif nums[curr] == 2:
                while two_pos >= 0 and nums[two_pos] == 2:
                    two_pos -= 1

                if nums[two_pos] == 0:
                    nums[zero_pos], nums[two_pos] = 0, 2
                    zero_pos += 1
                    two_pos -= 1
                else: # nums[two_pos] == 1:
                    nums[two_pos] = 2
                    two_pos -= 1

            curr += 1


        for i in range(zero_pos, two_pos + 1):
            nums[i] = 1

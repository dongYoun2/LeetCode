# submission: https://leetcode.com/problems/sort-colors/submissions/1903616571/
# runtime: 0 ms (Beats 100.00%), memory: 19.36 MB (Beats 29.71%)
# 18 min
# this solution actually solves the follow-up question, though i didn't see there exists the follow-up question at first.

# refer to the markdown file for the time and space complexity analysis.


# i noticed this is a dutch national flag problem, but i didn't remember the algortihm or whether it could be solve in one pass (on-the-fly). at first, i thought of two-pointer approach, and unconciously was trying to solve it in one pass. however, i realized it's much easier to solve in two passes. 

# since i wanted to solve in one pass first, then move on to two passes, i kept thinking when to swap the elements, and how it affects when reaching the later elements. so for the case when the current number is 0, i simply assigned it to the left pointer instead of swapping it. however, the second test case nums = [2,0,1] failed because of this. while debugging, i realized i also need to swap for this case and implemented it. but now, becuase i didn't increment the current index by 1 (`i += 1`) for the current number equals 0 case, my submission failed for the nums = [1, 2, 0] case (wrong submission: https://leetcode.com/problems/sort-colors/submissions/1903615658/). After fixing this, i was able to come up with the correct solution below where the logic is the same as the code in the markdown file.

# for more details, refer to the markdown file.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1

        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                continue
            i += 1

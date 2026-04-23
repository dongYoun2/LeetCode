# submission: https://leetcode.com/problems/max-consecutive-ones-ii/submissions/1986194858/
# runtime: 31 ms (beats 48.44%), memory: 19.57 MB (beats 75.36%)
# 8 min
# used sliding window technique.
# also solves the follow-up question.

# TC: O(n)
# SC: O(1)


# chose from a neetcode "sliding window" category.

# was pretty straightforward to solve. 

# for a better implementation, instead of using a boolean variable to track whether one zero has been flipped, we can use a integer count varaible to track the number of zeros in the current window. this submission can be found here: https://leetcode.com/problems/max-consecutive-ones-ii/submissions/1986225839/



class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        ans = l = 0
        flipped = False
        for r in range(n):
            if nums[r] == 0:
                if not flipped:
                    flipped = True
                else:
                    while nums[l] != 0:
                        l += 1
                    l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans

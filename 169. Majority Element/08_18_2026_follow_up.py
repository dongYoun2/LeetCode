# submission: https://leetcode.com/problems/majority-element/submissions/2112053819/
# runtime: 11 ms (beats 32.92%), memory: 21.29 MB (beats 18.50%)
# 7 min
# solved using Boyer-Moore Voting Algorithm (solves the follow-up question)

# refer to the README for a complexity analysis


# i saw my comments written on 08.11.2025 on Notion. it mentions that i solved the follow-up question using Boyer-Moore Voting Algorithm but the code itself ("08_11_2025_boyer_moore.py") was not neat. then, i was able to implement again with the logic below. the algorithm works as follows:

# 1. since in the problem statement, it is guaranteed that the majority element always exists, we can first assume and initialize the first element as the majority element.
# 2. then, we iterate through the array and count the occurrences of the majority element.
#   - if the current element is the same as the majority element, we increment the count.
#   - otherwise, we decrement the count, and if the count is less than 0, we update the majority element to the current element and reset the count to 1.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        cnt = 1

        for i in range(1, len(nums)):
            if nums[i] == ans:
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    ans = nums[i]
                    cnt = 1
        
        return ans

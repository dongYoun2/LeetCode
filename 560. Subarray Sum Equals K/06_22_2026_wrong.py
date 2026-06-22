# submission: https://leetcode.com/problems/subarray-sum-equals-k/submissions/2042141156/
# wrong answer
# 12 min
# attempted with a sliding window approach


# considering the problem constraints, i assumed i need to solve in O(n) time. while simulating, i thoguht this problem can be solved with a sliding window approach instead of DP approach, though prefix sum approach is also O(n) time algorithm (i think i was a little overfitted to the sliding window solution as i have recently practiced solving many sliding window problems).

# however, the solution below fails for the test case: nums = [1], k = 0.


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            
            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == k:
                ans += 1
        
        return ans

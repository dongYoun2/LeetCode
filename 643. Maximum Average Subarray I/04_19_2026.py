# submission: https://leetcode.com/problems/maximum-average-subarray-i/submissions/1982690954/
# runtime: 110 ms (beats 10.09%), memory: 29.37 MB (beats 21.45%)
# 11 min

# TC: O(n)
# SC: O(1)


# chose the problem from the "sliding window" category.

# pretty straightforward problem. i thought of starting directly with the fixed window size of k, but wanted to solve by adding one element at a time and then check if need to remove the leftmost element with the condition of keeping the window size of k (just like the problem "1888. Minimum Number of Flips to Make the Binary String Alternating").

# for the code where it directly starts with the fixed window size of k, refer to this submission: https://leetcode.com/problems/maximum-average-subarray-i/submissions/1982696695/.

# cf.) one minor improvement from the code below is to avoid the division of k in the loop, and instead, only keep the `max_sum` and do the division once at the end. (submission: https://leetcode.com/problems/maximum-average-subarray-i/submissions/1982692668/)


import math

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ans = -math.inf
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]

            if i >= k-1:
                ans = max(ans, curr_sum / k)
                curr_sum -= nums[i-k+1]
        
        return ans

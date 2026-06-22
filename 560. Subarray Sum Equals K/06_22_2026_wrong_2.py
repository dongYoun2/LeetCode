# didn't submit this solution since i could find the wrong test case beforehand


# realizing that the inputs and `k` can be negative, i changed the `while` loop condition from "06_22_2026_wrong.py", however this cannot completely solve the problem. the counter example is: nums = [1, -1, 1], k = 1.

# not only whhen the input integer is negative, this solution fails for the test case: nums= [0, 0, 0], and k = 0. expected answer is 6, but the solution returns 3. from this counterexample, i realized that this problem is essentailly the same as the problems "930. Binary Subarrays With Sum" or "713. Subarray Product Less Than K", but with allowing negative numbers. therefore, i tried writing a "06_22_2026_wrong_3.py" code.


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            
            while left < right and ((nums[left] > 0 and curr_sum > k) or nums[left] < 0 and curr_sum < k):
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == k:
                ans += 1
        
        return ans

[Problem](https://leetcode.com/problems/maximum-sum-circular-subarray/description/)

## Solution


### Corresponds to the LeetCode Editoral Approach 1

- [Submission](https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1659233010/)
<br>

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        normal_sum = curr_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(curr_sum, 0) + nums[i]
            normal_sum = max(normal_sum, curr_sum)

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        suffix_sum_dp = [0] * n
        suffix_sum_dp[n-1] = suffix_sum = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_sum += nums[i]
            suffix_sum_dp[i] = max(suffix_sum_dp[i+1], suffix_sum)

        special_sum = nums[0]
        for i in range(0, n-1):
            special_sum = max(special_sum, prefix_sum[i] + suffix_sum_dp[i+1])

        return max(normal_sum, special_sum)

```
<br>

## Corresponds to the LeetCode Editoral Approach 2

- [Submission](https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1659238060/)
<br>

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        curr_max = curr_min = 0
        max_sum = float('-inf')
        min_sum = float('inf')

        for x in nums:
            # accumulate total
            total_sum += x

            # Kadane for max subarray
            curr_max = max(curr_max + x, x)
            max_sum = max(max_sum, curr_max)

            # Kadane for min subarray
            curr_min = min(curr_min + x, x)
            min_sum = min(min_sum, curr_min)

        # If all numbers are negative, min_sum == total_sum,
        # so wrap case would empty out everything → invalid.
        if min_sum == total_sum:
            return max_sum

        print(max_sum, min_sum, total_sum)

        # Otherwise choose the better of non-wrap vs wrap
        return max(max_sum, total_sum - min_sum)

```
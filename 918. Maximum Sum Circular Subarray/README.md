[Problem](https://leetcode.com/problems/maximum-sum-circular-subarray/description/)


## Prefix–Suffix DP Approach (Same as the Editorial Approach 1)

This solution consider two cases, where the maximum subarray sum is either non-circular (Kadane's algorithm) or circular (prefix–suffix DP). For the non-circular case, the solution is straightforward by simply using Kadane's algorithm. For the circular case, the solution is the maximum value of the sum of the prefix and suffix sums with the condition that the number of elements in the subarray doesn't exceed the array length (buffer size) (Hint 2 provides the visual explanation that's easy to understand). To achieve this, we can precompute the maximum suffix sum (or either the maximum prefix sum) for each index in the array using the dynamic programming approach. More formally, `suffix_max[i] = max(suffix_max[i+1], suffix)`, where `suffix` is the running sum of the suffix starting from the end.

- [Submission](https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1820158503/) (Runtime: 131 ms, Memory: 22.32 MB)
- TC: $O(n)$, where $n$ is the length of `nums`.
- SC: $O(n)$


```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        # non-wrap (Kadane)
        curr = best = nums[0]
        for i in range(1, n):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)

        # prefix sums
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]

        # suffix max sums (running max of suffix sums using DP)
        suffix_max = [0] * n
        suffix_max[-1] = suffix = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix += nums[i]
            suffix_max[i] = max(suffix_max[i+1], suffix)

        # best wrap: split between i and i+1
        wrap_best = float("-inf")
        for i in range(n - 1):
            wrap_best = max(wrap_best, prefix[i] + suffix_max[i+1])

        return max(best, wrap_best)

```

## Dual Kadane’s Algorithm (Max + Min Trick) (Same as the Editorial Approach 2)

As mentioned above, the normal sum case, where the maximum subarray sum is not circular, can be solved by Kadane's algorithm. For the circular case, instead of thinking in terms of the prefix and suffix sums, we can think of it as where there's a gap (or a hole) in the subarray. Then, we want to find the minimum subarray sum (or the smallest hole) for this gap, and subtract it from the total sum to get the maximum subarray sum. One caveat is that if all the elements in the array are negative, the minimum subarray would the the entire array, and thus the maximum subarray sum would be the empty subarray, which is invalid as the problem statement explicitly requires non-empty subarray. therefore, we need to guard and return the maximum sum of the non-circular case.

cf.) I was so amazed by the simplicity and elegance of this approach when I first saw from the Editorial Section.

- [Submission](https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1659238060/) (Runtime: 100 ms, Memory: 21.13 MB)
- TC: $O(n)$
- SC: $O(1)$


```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        curr_max = curr_min = 0
        max_sum = float('-inf')
        min_sum = float('inf')

        for n in nums:
            # accumulate total
            total_sum += n

            # Kadane for max subarray
            curr_max = max(curr_max + n, n)
            max_sum = max(max_sum, curr_max)

            # Kadane for min subarray
            curr_min = min(curr_min + n, n)
            min_sum = min(min_sum, curr_min)

        # all-negative guard: wrapping would take the empty subarray
        if min_sum == total_sum:
            return max_sum

        # Otherwise choose the better of non-wrap vs wrap
        return max(max_sum, total_sum - min_sum)

```
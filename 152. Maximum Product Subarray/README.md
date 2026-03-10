[Problem](https://leetcode.com/problems/maximum-product-subarray/description/)


## Dynamic Programming

This solution is a natural extension of the Kadane's algorithm for the [maximum sum subarray problem](https://leetcode.com/problems/maximum-subarray/description/). Since there can exist negative numbers, we need to track the minimum product as well. Moreover, we need to reset the product when hitting zero. This will be automatically handled because when `nums[i]` is zero, `max_so_far` and `min_so_far` will both be zero, then in the next iteration, both will be updated to a new number because the candidates to check for the maximum and minimum product include the number itself, which will restart the product calculation.


[Submission](https://leetcode.com/problems/maximum-product-subarray/submissions/1944374172/)—Runtime: 7 ms (Beats 39.64%), Memory: 19.81 MB (Beats 70.63%)
- TC: $O(n)$, where $n$ is the length of the `nums` array
- SC: $O(1)$


```python
class Solution:
    def maxProduct(self, nums):
        max_so_far = min_so_far = nums[0]
        ans = max_so_far

        for i in range(1, len(nums)):
            cands = (nums[i], max_so_far * nums[i], min_so_far * nums[i])

            # min_so_far, _, max_so_far = sorted(cands)
            max_so_far, min_so_far = max(cands), min(cands)

            ans = max(ans, max_so_far)

        return ans

```



## Prefix-Suffix Scan

**Idea**: Scan the array from **both directions** while maintaining running products. This captures the maximum product subarray even when negatives flip the sign.

**Why it works**:
A negative number can turn a large negative product into a large positive one. By computing products left → right (prefix) and right → left (suffix), we effectively consider subarrays that may need to **exclude a prefix or suffix** when there is an odd number of negatives.


[Submission](https://leetcode.com/problems/maximum-product-subarray/submissions/1944377380/)—Runtime: 3 ms (Beats 90.83%), Memory: 19.74 MB (Beats 94.39%)
- TC: $O(n)$
- SC: $O(1)$

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = suffix = 1
        ans = nums[0]

        for i in range(n):
            # build prefix product (left → right)
            prefix *= nums[i]

            # build suffix product (right → left)
            suffix *= nums[n - 1 - i]

            ans = max(ans, prefix, suffix)

            # reset when hitting zero
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

        return ans

```
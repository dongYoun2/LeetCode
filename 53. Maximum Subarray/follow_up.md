[Problem](https://leetcode.com/problems/maximum-subarray/)

## Divide and Conquer Approach

This is the correct solution for the follow-up question. The main idea is to divide the array into two halves, recursively find the maximum subarray sum in each half, and also compute the **maximum subarray sum that crosses the midpoint**. The final result is the maximum of these three values. Note that the **maximum subarray sum that crosses the midpoint** is computed by finding the best suffix sum ending at the midpoint and the best prefix sum starting just after the midpoint.

Kadane's algorithm is a more efficient solution, but this divide and conquer approach is a valid alternative that works in $O(n \log n)$ time complexity. Also, it is a good exercise to understand how to break down problems recursively to solve it in a divide and conquer manner.


- [Submission](https://leetcode.com/problems/maximum-subarray/submissions/1652234138/) (Runtime: 1280 ms, Memory: 45.96 MB)
- TC: $O(n \log n)$, where $n$ is the length of `nums`.
- SC: $O(\log n)$ for recursion stack space.

```python
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert len(nums) > 0

        def compute_cross_max_sum(left, mid, right):
            """
            Return the max crossing subarray sum in [left..right].
            Always equals (best suffix ending at mid) + (best prefix starting at mid+1).
            """
            best_left = -math.inf
            left_sum = 0
            for i in range(mid, left - 1, -1):
                left_sum += nums[i]
                best_left = max(best_left, left_sum)

            best_right = -math.inf
            right_sum = 0
            for j in range(mid + 1, right + 1):
                right_sum += nums[j]
                best_right = max(best_right, right_sum)

            cross_max_sum = best_left + best_right

            return cross_max_sum


        def divide_and_conquer(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            left_best = divide_and_conquer(left, mid)
            right_best = divide_and_conquer(mid + 1, right)
            cross_best = compute_cross_max_sum(left, mid, right)

            return max([left_best, right_best, cross_best])


        return divide_and_conquer(0, len(nums) - 1)

```


In the above code, we computed the best prefix sum and the best suffix sum by iterating through the array in the `compute_cross_max_sum` function. However, this can be improved by directly returning the total sum, the maximum prefix sum, the maximum suffix sum, and the maximum subarray sum in the recursive function (corresponds to the `compute()` function below). Note that the runtime is ~4x faster than the above code.

cf.) This code is improved and refactored from the `10_31_2025_follow_up.py` code.

- [Submission](https://leetcode.com/problems/maximum-subarray/submissions/1817027125/) (Runtime: 285 ms, Memory: 45.80 MB)
- Time and space complexity are the same as the above.


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def compute(s, e):
            if s == e:
                # return (total, max_prefix, max_suffix, max_subarray)
                return nums[s], nums[s], nums[s], nums[s]

            m = (s + e) // 2
            l_total, l_prefix, l_suffix, l_best = compute(s, m)
            r_total, r_prefix, r_suffix, r_best = compute(m + 1, e)

            total = l_total + r_total
            prefix = max(l_prefix, l_total + r_prefix)
            suffix = max(r_suffix, r_total + l_suffix)
            best = max(l_best, r_best, l_suffix + r_prefix)

            return total, prefix, suffix, best


        return compute(0, len(nums) - 1)[3]

```


Though we could solve this problem with the **Divide and Conquer** approach, it's subtle and the Kadane's algorithm is much simpler and more efficient. (Simply good to practice the divide and conquer approach.)
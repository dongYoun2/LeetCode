[Problem](https://leetcode.com/problems/subarray-product-less-than-k/)


## Sliding Window (Optimal)

Refer to the `06_10_2026.py` for this approach.


## Prefix Sum + Binary Search

This approach is similar to the "930. Binary Subarrays With Sum" problem's Prefix Sum + Hash Table approach as described in the README.md of that problem. The only difference is that we need to use binary search instead of hash table to find the previous prefix product that is larger than `product / k`. The reasoning is as follows:

We need to find the previous prefix product $p$ such that:
$$
\frac{product}{p} < k \implies product < k \cdot p \implies p > \frac{product}{k}
$$

Cf.) The reason we need to use the hash table in the problem "930" is because we are looking for the exact sum that matches the target `goal`. 


[Submission](https://leetcode.com/problems/subarray-product-less-than-k/submissions/2029031662/)—Runtime: 4202 ms (beats 5.00%), Memory: 499.66 MB (beats 14.59%)

- TC: $O(n \log n)$, where $n$ is the length of the `nums` array
- SC: $O(n)$ (for the prefix sum array)


```python
from bisect import bisect_right

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        prefixes = [1]   # product before index 0
        product = 1
        count = 0

        for num in nums:
            product *= num

            # Need previous prefix p such that:
            # product / p < k
            # product < k * p
            # p > product / k
            idx = bisect_right(prefixes, product // k)

            count += len(prefixes) - idx

            prefixes.append(product)

        return count

```
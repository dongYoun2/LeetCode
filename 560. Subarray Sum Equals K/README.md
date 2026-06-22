[Problem](https://leetcode.com/problems/subarray-sum-equals-k/description/)



## Prefix Sum + Hash Table

This solution is similar to one of the solutions for the problem [930. Binary Subarrays With Sum](../930.%20Binary%20Subarrays%20With%20Sum/README.md). Also, the algorithm is conceptually the same as the Two Sum problem. The problem is basically **two sum on prefix sums**.

cf.) I was too overfitted to the sliding window solutions recently, lol.


[Submission](https://leetcode.com/problems/subarray-sum-equals-k/submissions/2042584983/)—Runtime: 92 ms (beats 5.96%), Memory: 23.51 MB (beats 6.31%)

- TC: $O(n)$
- SC: $O(n)$

```python
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1

        for num in nums:
            prefix += num
            count += seen[prefix - k]
            seen[prefix] += 1

        return count

```
[Problem](https://leetcode.com/problems/minimum-size-subarray-sum/)

## Sliding Window

- [Submission](https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1767716166/) (Runtime: 13 ms, Memory: 28.26 MB)
- TC: $O(n)$, where $n$ is the length of `nums`
- SC: $O(1)$

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = curr = 0
        ans = float('inf')

        for right, x in enumerate(nums):
            curr += x
            # shrink while valid
            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans

```

## Prefix Sum + Binary Search (Follow-up Question)

To solve this problem in $O(n \log n)$ time, we can use prefix sum and binary search. The reason we can use binary search is that the prefix sum array is strictly increasing  since all elements in `nums` are positive. While looking up the prefix sum in $O(1)$, we can loop through the indices of the prefix sum array (or `nums`), where this base index indicates the starting point of the subarray. Then, we can use binary search to find the smallest index `j` (ending point of the subarray) such that `prefix_sum[j] - prefix_sum[i] >= target`. The length of the subarray is `j - i`, and we can update the answer accordingly.

- [Submission](https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1767719618/) (Runtime: 55 ms, Memory: 28.61 MB)
- TC: $O(n \log n)$
- SC: $O(n)$ (for the prefix sum array)

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + nums[i - 1]  # prefix sums

        ans = float('inf')
        for i in range(n):  # start at i
            need = target + ps[i]
            # find the smallest j >= i+1 with ps[j] >= need
            j = bisect.bisect_left(ps, need, lo=i + 1)
            if j <= n:
                ans = min(ans, j - i)

        return 0 if ans == float('inf') else ans

```
[Problem](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/)

This problem felt very hard for me. Spent quite a long time to understand the solutions.

## Scanning All Possible Target Values

The key idea is to treat each number x as covering an interval [x-k, x+k], and for each possible target value, count how many numbers’ intervals include that target. Among those reachable numbers, at most numOperations can be changed, while existing copies of the target cost no operations, so the achievable frequency is $\min(\text{reachable},\ \text{count[target]} + \text{numOperations})$.


### Binary Search


[Submission](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/submissions/1979577663/)—Runtime: 472 ms (beats 48.14%), Memory: 36.36 MB (beats 61.40%)

Defining symbols:
- $n$: length of `nums`
- $V$: value range, which is the range of possible values of `nums` (`nums[-1] - nums[0] + 1`)
- $U$: number of unique values ($\leq n$)
<br>

- TC: $O(n \log n + V \log n)$
  - Sorting: $O(n \log n)$
  - Counter: $O(n)$
  - Binary search looping over all possible targets: $O(V \log n)$
- SC: $O(n)$ (Counter) 

```python
from collections import Counter
from bisect import bisect_left, bisect_right

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        cntr = Counter(nums)
        
        ans = 1
        for target in range(nums[0], nums[-1]+1):
            left = bisect_left(nums, target - k)
            right = bisect_right(nums, target + k)  # exclusive

            window_sz = right - left      # total reachable elements
            possible_freq = min(window_sz, cntr[target] + numOperations)
            ans = max(ans, possible_freq)
        
        return ans

```



### Sliding Window

[Submission](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/submissions/1979586051/)—Runtime: 323 ms (beats 82.56%), Memory: 36.47 MB (beats 51.86%)

- TC: $O(n \log n + V + n)$ -> $O(n \log n + V)$
  - Sorting: $O(n \log n)$
  - Counter: $O(n)$
  - Loop over all possible targets: $O(V)$
  - Pointers move at most $n$ times total
- SC: $O(n)$ (Counter) 


```python
from collections import Counter
from bisect import bisect_left, bisect_right

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        nums.sort()
        cntr = Counter(nums)
        
        ans = 1
        left = right = 0
        for target in range(nums[0], nums[-1]+1):
            while nums[left] < target - k:
                left += 1
            while right < n and nums[right] <= target + k:
                right += 1

            window_sz = right - left      # total reachable elements
            possible_freq = min(window_sz, cntr[target] + numOperations)
            ans = max(ans, possible_freq)
        
        return ans

```




## Dividing into Two Cases

Instead of scanning all possible target values, we can divide the problem into two cases:
1. The target value is an existing value in `nums`
2. The target value is NOT in `nums`





### Binary Search for the First Case

[Submission](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/submissions/1979585229/)—Runtime: 435 ms (beats 56.28%), Memory: 36.40 MB (beats 51.86%)

- TC: $O(n \log n + U \log n + n)$ -> $O(n \log n)$
  - Sorting: $O(n \log n)$
  - Counter: $O(n)$
  - Case 1: $O(U \log n)$
  - Case 2: $O(n)$ (classic sliding window pattern)
- SC: $O(n)$ (Counter)


```python
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        counter = Counter(nums)
        ans = max(counter.values())  # do nothing case

        # Case 1: target is an existing value in nums
        left = right = 0
        n = len(nums)

        for target in sorted(counter):
            left = bisect_left(nums, target - k)
            right = bisect_right(nums, target + k)  # exclusive

            reachable = right - left
            ans = max(ans, min(reachable, counter[target] + numOperations))

        # Case 2: target is NOT in nums
        left = 0
        for right in range(n):
            while nums[right] - nums[left] > 2 * k:
                left += 1

            window_size = right - left + 1
            ans = max(ans, min(window_size, numOperations))

        return ans

```



### Sliding Window for the First Case


[Submission](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/submissions/1979585135/)—Runtime: 388 ms (beats 63.25%), Memory: 36.32 MB (beats 61.40%)


- TC: $O(n \log n + U + n)$ -> $O(n \log n)$
  - Sorting: $O(n \log n)$
  - Counter: $O(n)$
  - Case 1: $O(U + n)$
  - Case 2: $O(n)$ (classic sliding window pattern)
- SC: $O(n)$ (Counter)


```python
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        counter = Counter(nums)
        ans = max(counter.values())  # do nothing case

        # Case 1: target is an existing value in nums
        left = right = 0
        n = len(nums)

        for target in sorted(counter):
            while nums[left] < target - k:
                left += 1
            while right < n and nums[right] <= target + k:
                right += 1

            reachable = right - left
            ans = max(ans, min(reachable, counter[target] + numOperations))

        # Case 2: target is NOT in nums
        left = 0
        for right in range(n):
            while nums[right] - nums[left] > 2 * k:
                left += 1

            window_size = right - left + 1
            ans = max(ans, min(window_size, numOperations))

        return ans

```
<br>

cf.) One important concept I learnt: behavior difference between `bisect_left` and `bisect_right` 

| Scenario             | `bisect_left` Result              | `bisect_right` Result               |
| :------------------- | :-------------------------------- | :---------------------------------- |
| Value not in list    | Same index (where it would go)    | Same index (where it would go)      |
| Value exists in list | Index of the **first** occurrence | Index **after** the last occurrence |

[Problem](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/)


## Sliding Window

- TC: $O(n \cdot k \log k)$
- SC: $O(k)$ (output space is not counted)

### Brute-Force (Rebuild the Counter for Each Window)

For each iteration, we rebuild the entire `counter` for the current window. Though this is inefficient, in this problem's input constraints, this is the most suitable and straightforward solution.

[Submission](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/submissions/1973960391/)—Runtime: 27 ms (beats 34.76%), Memory: 19.32 MB (beats 72.15%)

```python
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = [0] * (n-k+1)

        # window size == k
        for i in range(n-k+1):
            cntr = Counter(nums[i:i+k])
            cntr_sorted = sorted(cntr.items(), key=lambda item: (-item[1], -item[0]))
            answer[i] = sum(n*freq for n, freq in cntr_sorted[:x])
        
        return answer

```

### Expand-Shrink Pattern (Interview-friendly)

[Submission](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/submissions/1973959320/)—Runtime: 23 ms (beats 59.21%), Memory: 19.35 MB (beats 72.15%)

```python
from collections import defaultdict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cntr = defaultdict(int)
        answer = []

        def compute():
            items = sorted(cntr.items(), key=lambda it: (-it[1], -it[0]))
            return sum(v * freq for v, freq in items[:x])

        left = 0
        for right in range(len(nums)):
            # 1. add right
            cntr[nums[right]] += 1

            # 2. shrink if window too big
            if right - left + 1 > k:
                cntr[nums[left]] -= 1
                left += 1

            # 3. when window == k → compute
            if right - left + 1 == k:
                answer.append(compute())

        return answer

```
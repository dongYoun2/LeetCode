[Problem](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)


## (Lazy) Sliding Window + Two Monotonic Queues

The key idea of this problem is to find the min/max values of the current window efficiently. Time limit exceeded solutions ([06_16_2026_sorting_tle.py](06_16_2026_sorting_tle.py), [06_16_2026_counter_tle.py](06_16_2026_counter_tle.py)) recomputes the min/max values using either sorting or linear scan of the unique values every time the window changes. 

However, we can use two monotonic queues, one for finding minimum values and one for finding maximum values of the current window.

[Submission](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/2037921317/)—Runtime: 161 ms (beats 97.80%), Memory: 29.85 MB (beats 95.43%)

- TC: $O(n)$
- SC: $O(n)$

```python
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = deque()  # decreasing values: largest at front
        min_dq = deque()  # increasing values: smallest at front
        left = 0
        ans = 0

        for right, num in enumerate(nums):
            while max_dq and max_dq[-1] < num:
                max_dq.pop()
            max_dq.append(num)

            while min_dq and min_dq[-1] > num:
                min_dq.pop()
            min_dq.append(num)

            if max_dq[0] - min_dq[0] > limit:
                if nums[left] == max_dq[0]:
                    max_dq.popleft()
                if nums[left] == min_dq[0]:
                    min_dq.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans

```

cf.) We can simply change `if max_dq[0] - min_dq[0] > limit:` to `while max_dq[0] - min_dq[0] > limit:` if we want a typical sliding window approach (shrinking the window until the condition is met) instead of a lazy window shrinkage.



## (Lazy) Sliding Window + Two Heaps


Here, we use two heaps (min heap and max heap) to find the min/max values. One thing to note is that we also need to store the indices of the elements so that we can update the heaps with the `left` pointer.


[Submission](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/2037923786/)—Runtime: 343 ms (beats 24.32%), Memory: 43.06 MB (beats 7.21%)

- TC: $O(n \log n)$
- SC: $O(n)$

```python
import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []

        left = 0
        ans = 0

        for right, num in enumerate(nums):
            heapq.heappush(min_heap, (num, right))
            heapq.heappush(max_heap, (-num, right))

            if -max_heap[0][0] - min_heap[0][0] > limit:
                left += 1

                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)

                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)

            ans = max(ans, right - left + 1)

        return ans

```


cf.) We can simply change `if -max_heap[0][0] - min_heap[0][0] > limit:` to `while -max_heap[0][0] - min_heap[0][0] > limit:` if we want a typical sliding window approach instead of a lazy window shrinkage.
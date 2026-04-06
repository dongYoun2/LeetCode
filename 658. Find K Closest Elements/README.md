[Problem](https://leetcode.com/problems/find-k-closest-elements/)



## Binary Search on Window (Optimal w.r.t. TC)

The key idea is to perform binary search on the window of size `k` that contains `k` closest elements to `x`. Specifically, the target index is the left boundary (or the starting index) of this window.



[Submission](https://leetcode.com/problems/find-k-closest-elements/submissions/1970996737/)—Runtime: 0 ms (beats 100.00%), Memory: 20.62 MB (beats 71.21%)


- TC: $O(\log (n-k)$
- SC: $O(1)$


```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k  # possible window starts
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare which side is closer to x
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left + k]

```



## Binary Search + Two Pointers

This solution is the improved version of the `04_06_2026.py` solution.

Note that in the code below, the window is `(l, r)`, which excludes `arr[l]` and `arr[r]`. Since the window size is `r - l - 1`, we need to expand the window until the size reaches `k`.


[Submission](https://leetcode.com/problems/find-k-closest-elements/submissions/1970998597/)—Runtime: 1 ms (beats 74.72%), Memory: 20.74 MB (beats 50.70%)


- TC: $O(\log n + k)$
  - $O(\log n)$: binary search
  - $O(k)$: expanding pointers (or window)
- SC: $O(1)$


```python
import bisect
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = bisect.bisect_left(arr, x)
        
        l, r = pos - 1, pos
        
        # window is (l, r) -> excludes arr[l] and arr[r]
        # so the size of window == r - l - 1
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif x - arr[l] <= arr[r] - x:
                l -= 1
            else:
                r += 1
        
        return arr[l + 1:r]

```




## Sort by Distance


[Submission](https://leetcode.com/problems/find-k-closest-elements/submissions/1971003229/)—Runtime: 26 ms (beats 26.85%), Memory: 21.62 MB (beats 17.08%)

Note that since the original array `arr` is already sorted in ascending order, and the Python's `sort()` is stable, we can also simply do `arr.sort(key=lambda v: abs(v - x))` (instead of returning the tuple with the second argument `v`). So, if two values have the same distance to `x`, their original order is preserved, which matches the tie rule in the problem statement.


- TC: $O(n \log n)$
- SC: $O(\log n)$ (for built-in sorting)


```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # `arr.sort(key=lambda v: abs(v - x))` also works
        arr.sort(key=lambda v: (abs(v - x), v))
        return sorted(arr[:k])

```





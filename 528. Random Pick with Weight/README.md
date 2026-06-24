[Problem](https://leetcode.com/problems/random-pick-with-weight/)

I spent around 44 minutes to solve this problem, but couldn't solve it. Once I saw the solution, I was flabbergasted by the idea.


The core idea of this problem is to convert the weights into cumulative ranges using a prefix sum array. Instead of directly choosing an index, we randomly pick an integer from `[1, sum(w)]` and find which prefix-sum interval contains that number. In general, whenever probabilities are proportional to given weights, we should think of **weighted random sampling = prefix sum + search (linear or binary search)**.


## Naive Linear Scan (with a Running Cumulative Sum)

[Submission](https://leetcode.com/problems/random-pick-with-weight/submissions/2044834089/)—Runtime: 3956 ms (beats 6.12%), Memory: 23.92 MB (beats 99.53%)


- TC: 
  - `__init__`: $O(n)$
  - `pickIndex`: $O(n)$
- SC: 
  - `__init__`: $O(1)$
  - `pickIndex`: $O(1)$

```python
import random


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)

        curr_sum = 0
        for i, weight in enumerate(self.w):
            curr_sum += weight
            if curr_sum >= target:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

```


## Prefix Sum + Search



### Linear Search

Though this approach's time complexity analysis of `pickIndex` method is the same as the [Naive Linear Scan](#naive-linear-scan-with-a-running-cumulative-sum) solution, the actual runtime is faster in this approach because we precomputed the prefix sum array in the constructor instead of keeping a running cumulative sum in each `pickIndex` call (Note that `pickIndex` may be called at most $10^4$ times in the problem constraints.).


[Submission](https://leetcode.com/problems/random-pick-with-weight/submissions/2044836911/)—Runtime: 2474 ms (beats 13.08%), Memory: 24.54 MB (beats 67.82%)

- TC: 
  - `__init__`: $O(n)$
  - `pickIndex`: $O(n)$
- SC: 
  - `__init__`: $O(n)$
  - `pickIndex`: $O(1)$



```python
import random


class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []

        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.prefix.append(curr_sum)

        self.total = curr_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)

        for i, prefix_sum in enumerate(self.prefix):
            if prefix_sum >= target:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

```



### Binary Search (Optimal w.r.t. TC)


[Submission](https://leetcode.com/problems/random-pick-with-weight/submissions/2044841286/)—Runtime: 38 ms (beats 91.23%), Memory: 24.70 MB (beats 22.28%)


- TC: 
  - `__init__`: $O(n)$
  - `pickIndex`: $O(\log n)$
- SC: 
  - `__init__`: $O(n)$
  - `pickIndex`: $O(1)$



```python
import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        curr_sum = 0

        for weight in w:
            curr_sum += weight
            self.prefix.append(curr_sum)

        self.total = curr_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

```
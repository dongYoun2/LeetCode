[problem](https://leetcode.com/problems/design-hit-counter/)


There are several approaches to solve this problem. [Queue-based Approach](#queue-based-approach) and [Fixed Array of Size 300](#fixed-array-of-size-300-solves-the-follow-up-question) solutions are usually regarded easy to come up with and to implement during the interview.



## Binary Search-based Approach



### Pure Binary Search

[Submission](https://leetcode.com/problems/design-hit-counter/submissions/2051763490/)—Runtime: 0 ms (beats 100.00%), Memory: 19.49 MB (beats 40.07%)

Symbols: 
- $n$: number of hits
- $u$: unique timestamps ($u \leq n$)


TC: 
- `hit()`: $O(1)$
- `getHits()`: $O(\log n)$

SC: 
- entire object: $O(n)$

```python
import bisect


class HitCounter:

    def __init__(self):
        self.hits = []


    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        idx = bisect.bisect_right(self.hits, timestamp - 300)

        return len(self.hits) - idx

```



### Prefix Sum + Binary Search (Solves the Follow-up Question)

Refer to the [06_30_2026.py](06_30_2026.py) file.




## Queue-based Approach

The key observation is that we only need the number of hits in the last 300 seconds. From this, we can infer that a FIFO data structure (queue) is suitable.


### Plain Queue


[Submission](https://leetcode.com/problems/design-hit-counter/submissions/2051775669/)—Runtime: 3 ms (beats 14.00%), Memory: 19.58 MB (beats 11.97%)

Symbols are the same as in the [Pure Binary Search](#pure-binary-search) section.

TC: 
- `hit()`: $O(1)$
- `getHits()`: amortized $O(1)$, worst $O(n)$

SC: 
- entire object: $O(n)$


```python
from collections import deque


class HitCounter:

    def __init__(self):
        self.hits = deque()  # stores every hit timestamp


    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()

        return len(self.hits)

```



### Queue of (timestamp, count) Pairs (Solves the Follow-up Question)



[Submission](https://leetcode.com/problems/design-hit-counter/submissions/2051776840/)—Runtime: 0 ms (beats 100.00%), Memory: 19.42 MB (beats 40.07%)

Symbols are the same as in the [Pure Binary Search](#pure-binary-search) section.

TC: 
- `hit()`: $O(1)$
- `getHits()`: amortized $O(1)$, worst $O(u)$

SC: 
- entire object: $O(u)$


```python
from collections import deque


class HitCounter:

    def __init__(self):
        self.hits = deque()  # stores [timestamp, count]
        self.total = 0


    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, 1])

        self.total += 1


    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][0] <= timestamp - 300:
            old_time, old_count = self.hits.popleft()
            self.total -= old_count

        return self.total

```



## Fixed Array of Size 300 (Solves the Follow-up Question)

This solution is clever. We only need two arrays; no need of other data structures such as queue. We can leverage the **modulo operation** to find the corresponding index of the current timestamp and the hit count.



[Submission](https://leetcode.com/problems/design-hit-counter/submissions/2051777890/)—Runtime: 0 ms (beats 100.00%), Memory: 19.39 MB (beats 76.36%)

Symbols are the same as in the [Pure Binary Search](#pure-binary-search) section.

TC: 
- `hit()`: $O(1)$
- `getHits()`: $O(300) = O(1)$

SC: 
- entire object: $O(300) = O(1)$


```python
class HitCounter:

    def __init__(self):
        self.times = [0] * 300
        self.counts = [0] * 300


    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300

        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.counts[idx] = 1
        else:
            self.counts[idx] += 1


    def getHits(self, timestamp: int) -> int:
        total = 0

        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.counts[i]

        return total

```
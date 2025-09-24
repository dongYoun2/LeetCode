[Problem](https://leetcode.com/problems/task-scheduler/)


## Greedy with Priority Queue


The code below is the optimized version of the solution in `09_24_2025.py`. Instead of building the intervals, we only need to return the number of intervals (time).

To achieve this, we only need to store the frequency of each task, and we can accumulate the elapsed time every cycle (or batch), which is simply `n + 1`. One caveat is that for the last cycle, we don't need the full `n + 1` time, but the number of tasks that are processed in the last cycle.

[Submission](https://leetcode.com/problems/task-scheduler/submissions/1781571914/) (Runtime: 64 ms, Memory: 19.23 MB)


Symbols:
- $T$: total task instances (length of tasks)
- $K$: number of unique tasks (number of capital letters == 26)

TC:
- building Counter and heap: $O(T) + O(K)$
- Each task instance is popped once ($O(\log k)$) and (unless it finishes) pushed once ($O(\log k)$). So, across all tasks: $O(T \log K)$
- therefore: $O(T + K + T \log K)$ -> $O(T \log K + K)$ -> $O(T)$ (since $K$ is bounded by 26)

SC:
- Counter: $O(K)$
- heap: $O(K)$
- therefore: $O(K)$


```python
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        freq = Counter(tasks).values()
        heap = [-c for c in freq]

        heapq.heapify(heap)

        time = 0
        while heap:
            executed = 0
            to_requeue = []

            for _ in range(n + 1):
                if not heap:
                    break
                cnt = heapq.heappop(heap) + 1  # run one instance
                executed += 1
                if cnt < 0:
                    to_requeue.append(cnt)

            for cnt in to_requeue:
                heapq.heappush(heap, cnt)

            time += (n + 1) if heap else executed

        return time

```

## Filling the Vacant Slots with Sorting

This solution is based on the idea of filling the vacant slots with the most frequent tasks. It is still a greedy approach, but more efficient than the priority queue approach.

Additionally, we can optimize the sorting to simply using the max frequency, which leads to a $O(T + K)$ time complexity (unlike $O(T + K \log K)$), when the $K$ grows.

cf.) Further extending this approach would lead to a math formula solution. Refer to the [Editorial's Approach 4](https://leetcode.com/problems/task-scheduler/editorial/#approach-4-using-math-formula) for more details.


- [Submission](https://leetcode.com/problems/task-scheduler/submissions/1781657297/) (Runtime: 19 ms, Memory: 19.00 MB)
- TC: $O(T + K \log K + K)$ -> $O(T + K \log K)$ -> $O(T)$ (since $K$ is bounded)
  - Building Counter: $O(T)$
  - Sorting (`most_common()`): $O(K \log K)$
  - Filling the vacant slots: $O(K)$
- SC: $O(K)$ (Frequency map; the list)


```python
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cntr = Counter(tasks)
        freq = [cnt for _, cnt in cntr.most_common()]
        max_freq = freq[0]

        batch_cnt = max_freq - 1  # X need to consider last batch
        vacant_cnt = batch_cnt * n

        for i in range(1, len(freq)):
            vacant_cnt -= min(batch_cnt, freq[i])  # use min(): only batch_cnt slots can be filled, even if freq[i] == max_freq

        return len(tasks) + vacant_cnt if vacant_cnt > 0 else len(tasks)

```
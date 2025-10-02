[Problem](https://leetcode.com/problems/meeting-rooms-ii/description/)

## Using Priority Queue


To come up with the priority queue (min heap) solution, we have to first think about how we can better assign an existing meeting room instead of scanning through all of the rooms. This leads to a **min heap** data structure to effectively find a meeting room that **ends earliest** (note that our meetings (`intervals`) are ordered by the start time).

**Comparing with `10_02_2025.py` implementation**

Instead of storing the intervals (or meetings) themselves with the end time as the key in the priority queue, which is the way it's done in the `10_02_2025.py`, we can simply store only the end times as the keys. Also, we don't have to pop all the meeting rooms that already ended, and instead we can simply check whether the current meeting's start time is greater than the earliest end time in the priority queue. if it is,  we can pop the earliest end time, and if not, we can increment the number of rooms (the answer) by 1.


- [Submission](https://leetcode.com/problems/meeting-rooms-ii/submissions/1789391349/) (Runtime: 3 ms, Memory: 19.90 MB)
- TC: $O(n \log n + n \log n)$ -> $O(n \log n)$, where $n$ is the length of the `intervals`.
  - Sorting takes $O(n \log n)$ time.
  - Each heappop/heappush takes $O(\log n)$ time and since we are doing either of these operations for all intervals, it takes $O(n \log n)$ time.
  - Therefore, $O(n \log n)$ in total.
- SC: $O(n)$, for the heap.


```python
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda elem: elem[0])

        end_times = [intervals[0][1]]   # maintain only end times using min heap
        room_cnt = 1
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]

            if end_times[0] <= curr_interval[0]:    # heap peek with `end_times[0]`
                heapq.heappop(end_times)
            else:
                room_cnt += 1

            heapq.heappush(end_times, curr_interval[1])

        return room_cnt # `return len(end_times)` also works

```
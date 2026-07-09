[Problem](https://leetcode.com/problems/meeting-rooms-ii/description/)

A **key point** for this problem is: when a meeting starts, we only need to know whether the earliest-ending active meeting has already finished.

## Using Priority Queue

**Pattern recognition cue**: whenever we need the maximum number of overlapping intervals at any point in time, think: sort by start time and track end times with a min heap.

To come up with the priority queue (min heap) solution, we have to first think about how we can better assign an existing meeting room instead of scanning through all of the rooms. This leads to a **min heap** data structure to effectively find a meeting room that **ends earliest** (note that our meetings (`intervals`) are ordered by the start time).


**Why we need to sort by the start time, not the end time?**

Because room allocation decisions happen when a meeting starts. For each meeting, we compare its start time with the earliest ending active meeting to decide whether a room can be reused or a new room is needed, and this can be done efficiently with a priority queue.

Sorting by **end time** is common in interval-greedy problems where the goal is to maximize coverage or minimize selections. For example, in [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/), sorting by end time lets us place an arrow at the earliest possible position and burst the maximum number of overlapping balloons.


**Comparison with `10_02_2025.py` implementation**

Instead of storing the intervals (or meetings) themselves with the end time as the key in the priority queue, which is the way it's done in the `10_02_2025.py`, we can simply store only the end times as the keys. Also, we don't have to pop all the meeting rooms that already ended, and instead we can simply check whether the current meeting's start time is greater than the earliest end time in the priority queue. if it is,  we can pop the earliest end time, and if not, we can increment the number of rooms (the answer) by 1.


[Submission](https://leetcode.com/problems/meeting-rooms-ii/submissions/2062163949/)—Runtime: 7 ms (beats 25.65%), Memory: 21.39 MB (beats 79.53%)

- TC: $O(n \log n + n \log n)$ -> $O(n \log n)$, where $n$ is the length of the `intervals`.
  - Sorting takes $O(n \log n)$ time.
  - Each heappop/heappush takes $O(\log n)$ time and since we are doing either of these operations for all intervals, it takes $O(n \log n)$ time.
  - Therefore, $O(n \log n)$ in total.
- SC: $O(n)$, for the heap.


```python
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        end_times = [intervals[0][1]]   # maintain only end times using min heap

        for i in range(1, n):
            if end_times[0] <= intervals[i][0]: # heap peek with `end_times[0]`
                heapq.heappop(end_times)
            
            heapq.heappush(end_times, intervals[i][1])
        
        return len(end_times)
 
```
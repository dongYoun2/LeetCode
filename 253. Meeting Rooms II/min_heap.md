## Using Min Heap

To come up with the min heap solution, we have to first think about how we can better assign an existing meeting room instead of scanning through all of the rooms. This leads to a **min heap** data structure to effectively find a meeting room that **ends earliest** (meetings are ordered by the start time). Time complexity and space complexity for this solution are $O(n \log n)$ and $O(n)$, respectively.


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
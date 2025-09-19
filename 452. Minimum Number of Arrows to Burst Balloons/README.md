[Problem](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)


## Optimal Greedy Approach

This approach is more optimal than the `09_19_2025.py` solution. The idea is to sort the `points` array based on the **end position** of the points. Then, we can iterate through the `points` array and keep track of the previous end position. If the current point's start position is greater than the previous end position, we need to increment the answer.

The greedy propety is simpler if sort by the **end position** because the optimal strategy is always: **“Shoot an arrow at the earliest finishing balloon’s end, and burst all overlapping ones in one shot.”** In words, we want to place the arrow as far right as possible. The advantage of this is that we don't need to track/shrink the overlapping intervals (windows) anymore (removes `max()` and `min()` operations).

- [Submission](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/1776219581/) (Runtime: 59 ms, Memory: 51.4 MB)
- TC: $O(n log n)$, where $n$ is the length of the `points` array.
- SC: $O(1)$

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        assert len(points) > 0

        # Sort by right endpoint (xend)
        points.sort(key=lambda interval: interval[1])

        ans = 1
        prev_xend = points[0][1]

        for i in range(1, len(points)):
            xstart, xend = points[i]
            if xstart > prev_xend:
                ans += 1
                prev_xend = xend  # place arrow at the tightest spot

        return ans

```
# submission: https://leetcode.com/problems/k-closest-points-to-origin/submissions/1832462814/
# runtime: 19 ms, memory: 21.93 MB

# 2 min
# TC: O(n log n), where n is the number of points
# SC: O(1)

# most straightforward solution is simply sorting the points and returning the first k points. the time complexity for this approach is O(n log n).

# there are several other approaches to solve this problem, including using heap (priority queue) and quick-select, where time complexity is O(n log k) and O(n) respectively.


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:k]

# problem: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# submission: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/1602829506/


# 23 min
# TC: O(n log n), where n is the number of balloons (points)
# SC: O(n + n) -> O(n) (n for python timsort and n for intersected_points)
# Refer to the Editorial's Approach 1 for the optimal solution.

# From LeetCode Top Interview 150 - Intervals

# The below solution takes a greedy approach to intervals. First, I sorted the points (balloons) based on the "start" position. Afterward, I kept track of the intervals' intersections, which are stored in `intersected_points`. Then, the minimum number of arrows needed is equal to the number of intersected points.

# However, this solution is not optimal in practice. The better approach is to sort the points based on the "end" position. This way, we don't need to keep track of the intersections. Instead, we can just check whether the current point's "start" position is less than or equal to the previous "end" position that we are keeping track of. This is more reasonable to think of it as a greedy algorithm since we want the arrow to be as far right as possible. For more details, refer to the Editorial's Approach 1.

# Although the suboptimal and optimal solutions are the same in time and space complexity, the first approach runs slower in practice due to additional overhead, such as keeping track of the (most recent) intersection and min/max operations.

# Since I have been solving interval problems recently, I think I unconsciously (or habitually) sorted based on the "start" position (or without too much attention). I should remind myself that every line of code has to have a purpose lol.


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        intersected_points = [points[0]]
        for i in range(1, len(points)):
            start, end = points[i]

            if start <= intersected_points[-1][1]:
                intersected_points[-1][0] = max(intersected_points[-1][0], start)
                intersected_points[-1][1] = min(intersected_points[-1][1], end)
            else:
                intersected_points.append(points[i])

        return len(intersected_points)


# notes while solving the problem:

# 1    6
#   2          8
#                    10        16
#           7             12


# 1    2
#      2      3
#             3      4
#                    4       5

# greedy?
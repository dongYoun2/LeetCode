# submission: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/1776204647/
# runtime: 143 ms, memory: 51.5 MB

# 15 min
# TC: O(n log n), where n is the length of the `points` array.
# SC: O(1)

# this is a second time solving this problem. i remember that i could solve using a greedy approach, so i assumed it so. also, noticing maximum length of the `points` array is 100K, i assumed i need to sovle it in O(n log n) time, which feels like i need to sort the `points` array. considering all these, i simulated for provided two cases, and could implement the code below.

# however, more optimal solution is sorting based on the end position of the points. for more details, refer to the markdown file.


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        ans = 1
        prev_s, prev_e = points[0]

        for i in range(1, len(points)):
            s, e = points[i]

            if s <= prev_e:
                prev_s = max(prev_s, s)
                prev_e = min(prev_e, e)
            else:
                prev_s, prev_e = s, e
                ans += 1

        return ans

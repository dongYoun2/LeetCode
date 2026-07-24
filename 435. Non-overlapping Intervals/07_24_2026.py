# submission: https://leetcode.com/problems/non-overlapping-intervals/submissions/2080054222/
# runtime: 175 ms (beats 16.25%), memory: 49.04 MB (beats 55.20%)
# 18 min
# solved with a greedy approach

# TC: O(n log n + n) -> O(n log n)
# SC: O(1)


# intervals problem usually requires sorting. from the input constraints (n <= 100K), i was sure the sorting is needed. then, the intervals problem generally requires algorithm that takes linear time so that the total time complexity becomes O(n log n). i suspected the greedy approach, and think in that way. the key greedy idea is keeping the earliest end time among the current and the previous intervals. since, i sorted by the start time in the code below, i needed to explicitly use the `min()` function.

# however, simpler and more straightforward solution is to sort by the end time. once we sort by the end time, the runtime becomes faster in practice (though the time complexity is the same) due to the no use of the `min()` function. the code can be found here: https://leetcode.com/problems/non-overlapping-intervals/submissions/2080069209/—runtime: 88 ms (beats 45.06%), memory: 49.01 MB (beats 55.20%)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()    # sort by the start time
        ans = 0

        _, prev_e = intervals[0]
        for i in range(1, n):
            curr_s, curr_e = intervals[i]

            if prev_e > curr_s:
                ans += 1
                prev_e = min(prev_e, curr_e)
            else:
                prev_e = curr_e
        
        return ans

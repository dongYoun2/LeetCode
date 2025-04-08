# problem: https://leetcode.com/problems/merge-intervals/
# submission: https://leetcode.com/problems/merge-intervals/submissions/1600826088/

# 8 min
# TC: O(n log n + n) -> O(n log n)
# SC: O(n) (Python timsort worst-case. Answer array is not counted.)

# From LeetCode Top Interview 150 - Intervals

# This is my second time solving this problem. I have solved this on Feb 16, 2025.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda elem: elem[0])

        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            last_interval = ans[-1]

            if curr_interval[0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], curr_interval[1])
            else:
                ans.append(curr_interval)

        return ans

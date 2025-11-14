# problem: https://leetcode.com/problems/insert-interval/
# submission: https://leetcode.com/problems/insert-interval/submissions/1601822668/
# runtime: 0 ms, memory: 19.74 MB

# 9 min
# TC: O(n log n)
# SC: O(n) (Python timsort. output list is not counted.)


# From LeetCode Top Interview 150 - Intervals

# This is the second time solving this problem. I have solved this on Nov 25, 2024.

# Since I solved "56. Merge Intervals" yesterday, I came up the solution below quite easily. After appending `newInterval` to `intervals`, the rest logic is exactly the same as "56. Merge Intervals".

# cf.) in the problem descrption, it mentions that the intervals are already sorted by the start time. so, actually, we don't need to sort the intervals again.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])

        return ans

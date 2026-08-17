# submission: https://leetcode.com/problems/insert-interval/submissions/1601822668/
# runtime: 0 ms (beats 100.00%), memory: 19.74 MB (beats 100.00%)
# 9 min
# append new interval + sorting + mege with linear scan

# TC: O(n log n + n) -> O(n log n) (sorting + linear scan)
# SC: O(n) (Python timsort requires O(n) temporary space; output list is not counted)


# From LeetCode Top Interview 150 - Intervals

# second time solving this problem. I have solved this problem on Nov 25, 2024.

# Since I solved "56. Merge Intervals" yesterday, I was able to come up with the below solution quite easily. After appending `newInterval` to `intervals`, the rest logic is exactly the same as the problem "56. Merge Intervals".

# cf.) in the problem descrption, it mentions that the intervals are already sorted by the start time. so, actually, we can use binary search to find the insertion position of `newInterval`, which requires O(log n) time complexity.


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

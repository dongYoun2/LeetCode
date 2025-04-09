# problem: https://leetcode.com/problems/insert-interval/
# submission: https://leetcode.com/problems/insert-interval/submissions/1601839693/

# TC: O(log n + 2*n) -> O(n) (binary search + inserting newInterval + merge)
# SC: O(1) (output list is not counted)

# cf.) If I use `intervals = intervals[:i] + [newInterval] + intervals[i:]`instead of `intervals.insert(i, newInterval)`, the space complexity will be O(n) because it creates a new list and copies the elements. Moreover, `insert()` preserves the memory address, whereas the slicing creates a new list with a different memory address.

# From LeetCode Top Interview 150 - Intervals

# After solving with Python sorting ("04_09_2025.py"), I found out that  I can also use the binary search to find the position to insert `newInterval`, preserving the sorted order of `intervals`.


from bisect import bisect_left

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = bisect_left(intervals, newInterval[0], key=lambda e: e[0])

        intervals.insert(i, newInterval)    # alternative: intervals = intervals[:i] + [newInterval] + intervals[i:]

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])

        return ans

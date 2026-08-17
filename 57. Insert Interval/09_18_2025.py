# submission: https://leetcode.com/problems/insert-interval/submissions/1775535414/
# runtime: 0 ms (beats 100.00%), memory: 19.89 MB (beats 100.00%)
# 39 min
# Find overlap boundaries with linear search, then merge

# TC: O(n)
# SC: O(1)


# at first, i knew i could solve this problem after sorting, but that would require O(n log n) time complexity (just like "04_09_2025.py"); but note that the intervals are already sorted by the start time, lol.

# so, i tried to solve it in O(n) time. after failing on several cases (submitting and fixing on and on; trial and error), i finally could solve it with the code below. especially, i found it's easier to think even with defining the `mid_intervals` where the start of the new interval is equal to the start of the intervals in the input.

# however, the code is not very readable and it could be improved further. for more details, refer to the markdown file.


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        prev_intervals = [elem for elem in intervals if elem[0] < newInterval[0]]
        mid_intervals = [elem for elem in intervals if elem[0] == newInterval[0]]
        next_intervals = [elem for elem in intervals if elem[0] > newInterval[0]]

        for _, e in mid_intervals:
            newInterval[1] = max(newInterval[1], e)


        if prev_intervals and prev_intervals[-1][1] >= newInterval[0]:
            e = prev_intervals.pop()
            newInterval[0] = e[0]
            newInterval[1] = max(newInterval[1], e[1])

        curr = -1
        for i in range(len(next_intervals)):
            if next_intervals[i][0] > newInterval[1]:
                break
            newInterval[1] = max(newInterval[1], next_intervals[i][1])
            curr = i

        return prev_intervals + [newInterval] + next_intervals[curr+1:]

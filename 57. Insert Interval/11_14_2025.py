# submission: https://leetcode.com/problems/insert-interval/submissions/1829813921/
# runtime: 3 ms (beats 29.88%), memory: 19.89 MB (beats 100.00%)
# 8 min
# Find overlap boundaries with linear search, then merge

# TC: O(n), where n is the number of intervals
# SC: O(n) `front`, `middle`, `rear` arrays are used to store the intervals. (output space not counted)


# this is pretty simple and straightforward solution. note that the input intervals are already sorted by the start time.


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        front, middle, rear = [], [], []
        for inter in intervals:
            if inter[1] < newInterval[0]:
                front.append(inter)
            elif inter[0] > newInterval[1]:
                rear.append(inter)
            else:
                middle.append(inter)

        new_inter_s = min([s for s, _ in middle] + [newInterval[0]])
        new_inter_e = max([e for _, e in middle] + [newInterval[1]])

        return front + [[new_inter_s, new_inter_e]] + rear

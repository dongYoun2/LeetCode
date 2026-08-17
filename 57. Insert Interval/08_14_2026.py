# submission: https://leetcode.com/problems/insert-interval/submissions/2107033261/
# runtime: 4 ms (beats 12.61%), memory: 21.36 MB (beats 56.80%)
# 16 min
# Find overlap boundaries with linear search, then merge (the logic is exactly the same as "11_14_2025.py")


# at first, i tried to implement in a one-pass solution, but was a little tricky. i realized i can simply find all the previous and next intervals that cannot be merged with the new interval. then the rest will be overlapping intervals, so i found the min start and max end of those intervals plus the new interval.

# however, as mentioned in the README's "Linear Search: Element", we don't need to find all overlapping intervals. we only need the first and last overlapping intervals. this allows us to compute min start and max end in constant time. refer to the README for more details and concise solution.


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        before = [[s, e] for s, e in intervals if e < newInterval[0]]
        after = [[s, e] for s, e in intervals if newInterval[1] < s]
        to_merge = [[s, e] for s, e in intervals if not (e < newInterval[0]) and not (newInterval[1] < s)]
        to_merge.append(newInterval)

        merged_interval = [min(s for s, _ in to_merge), max(e for _, e in to_merge)]

        return before + [merged_interval] + after

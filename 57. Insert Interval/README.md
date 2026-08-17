[Problem](https://leetcode.com/problems/insert-interval/)



## One-pass Scan + Merge on the Fly

[Submission](https://leetcode.com/problems/insert-interval/submissions/2110394512/)—Runtime: 3 ms (beats 29.88%), Memory: 21.25 MB (beats 89.11%)


- TC: $O(n)$
- SC: $O(1)$ (output space not counted)


```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)

        # 1. Intervals completely before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        ans.append(newInterval)

        # 3. Intervals completely after newInterval
        ans.extend(intervals[i:])

        return ans

```



## Find Overlap Boundaries with Linear Search + Merge

Unlike the ["One-pass Scan + Merge on the Fly"](#one-pass-scan-merge-on-the-fly) solution, this approach splits into two steps: first finds the insertion/overlap boundaries with linear search, then merges the intervals. 




### Using List Comprehension


Note that we only need to find the `left` (intervals that end before the new interval starts) and `right` (intervals that start after the new interval ends) intervals. We don't need to separately find the overlapping intervals like in the [08_14_2026.py](08_14_2026.py) since we can simply use `left` and `right` length to directly access the first overlapping interval (`intervals[len(left)]`), which has the smallest start time, and the last overlapping interval (intervals[-len(right)-1]), which has the largest end time, to compare with the `newInterval`.


[Submission](https://leetcode.com/problems/insert-interval/submissions/2110401238/)—Runtime: 40 ms (beats 5.68%), Memory: 21.33 MB (beats 56.97%)


- TC: $O(n)$
- SC: $O(n)$


```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        left = [inter for inter in intervals if inter[1] < s]
        right = [inter for inter in intervals if inter[0] > e]

        if len(left) + len(right) != len(intervals):
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[-len(right)-1][1])

        return left + [[s, e]] + right

```


### Index-based Approach


Since we find start and end indicies of interval to merge, the space complexity reduces to $O(1)$.


[Submission](https://leetcode.com/problems/insert-interval/submissions/2110409973/)—Runtime: 0 ms (beats 100.00%), Memory: 21.45 MB (beats 26.78%)

- TC: $O(n)$
- SC: $O(1)$


```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
        
        j = len(intervals) - 1
        while j >= 0 and intervals[j][0] > newInterval[1]:
            j -= 1

        if j >= i:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[j][1])

        return intervals[:i] + [newInterval] + intervals[j+1:]

```




## Find Insertion/Boundaries with Binary Search + Merge

Refer to the [04_09_2025_binary_search.py](04_09_2025_binary_search.py) file for the solution.

[Problem](https://leetcode.com/problems/insert-interval/)

## Linear Search: Element
The below solutions use linear search. With this approach, there is no need to use binary search (in addition to merging, which already requires $O(n)$ time complexity) in `04_09_25_binary_search.py`, nor a sorting algorithm like `04_09_2025.py`, which has $O(n log(n))$ time complexity.

- [Submission](https://leetcode.com/problems/insert-interval/submissions/1226700284/)
- TC: $O(n)$
- SC: $O(n)$ (Output array is not counted. Additional storage is for `left` and `right`.)

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
<br>


## Linear Search: Index

- [Submission](https://leetcode.com/problems/insert-interval/submissions/1601968794/)
- TC: $O(n)$
- SC: $O(1)$

Since we find start and end indicies of interval to merge, the space complexity reduces to $O(1)$.


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
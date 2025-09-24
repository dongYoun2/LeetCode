[Problem](https://leetcode.com/problems/daily-temperatures/)

## Monotonic Stack Approach


The core idea is to maintain a monotonic (decreasing) stack. We are storing the indices of the temperatures, where those temperatures are in descending order. (You can find the simulation in the Editoral section)

cf.) **Monotonic stack is commonly used** to solve problems where you need to quickly find the next greater element, next smaller element, previous greater element, or previous smaller element in an array.

Example problems includes: Largest Rectangle in Histogram, Trapping Rain Water, Stock Span Problem, etc.



- [Submission](https://leetcode.com/problems/daily-temperatures/submissions/1781394089/) (Runtime: 88 ms, Memory: 26.92 MB)
- TC: $O(N)$, where N is the length of temperatures
- SC: $O(N)$


```python
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = deque()

        for curr_day in range(n):
            curr_temp = temperatures[curr_day]

            # Pop colder days from the stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day

            stack.append(curr_day)

        return ans

```

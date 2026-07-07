[Problem](https://leetcode.com/problems/largest-number/)


## Custom Comparator-based Sorting


I spent half an hour on this problem, but couldn't solve it. It's obvious that we first choose the number with the larger leftmost digit. However, the issue was when there are, for example [3, 30, 34] left, how to choose? the largest number is 34330. From this example, I noticed when we are comparing only two numbers, we can simply concatenate them and compare the result. if we can decide the order of two elements (or numbers), that simply becomes the logic of the comparator function. I completely forgot about this comparator function feature, which many programming languages, such as, Javascript, Golang, and of course, Python, etc. support. So, this problem was a good reminder for a use case of the comparator function.



[Submission](https://leetcode.com/problems/largest-number/submissions/2058047476/)—Runtime: 3 ms (beats 64.94%), Memory: 19.10 MB (beats 90.91%)

- TC: $O(k n \log n)$, where $n$ is the length of the input array, and $k$ is the maximum number of digits of the numbers in the array (From the problem constraints, $1 \leq n \leq 100$ and $1 \leq k \leq 10$)
- SC: $O(nk)$ (the `strs` array)


```python
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(num) for num in nums]

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1   # a should come first
            elif a + b < b + a:
                return 1    # b should come first
            return 0

        strs.sort(key=cmp_to_key(compare))

        result = ''.join(strs)

        return '0' if result[0] == '0' else result

```
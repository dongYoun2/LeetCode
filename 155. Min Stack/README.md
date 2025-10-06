[Problem](https://leetcode.com/problems/min-stack/)

Below is the code that I wrote while solving the above problem on Apr 16, 2024 lol.

Unlike `04_12_2025.py` solution, we could solve the problem without using any if-else conditions. There are two points.

1. Initialize `min_stack` with $2^{31}$, where $2^{31}$ is the one added value from the maximum value that the `val` can take. This is to not consider the (exception) case where `stack` (or `min_stack`) is pushed when it is empty. (This is analogous to using the dummy nodes in a linked list.)
2. Keep the `min_stack` length the same as `stack` (technically, `len(min_stack) == len(stack) + 1`). Whenever we push or pop the stack, we can also perform the same operation on the `min_stack`.

- [Submission](https://leetcode.com/problems/min-stack/submissions/1234483546/) (Runtime: 50 ms, Memory: 20.28 MB)
- TC: all methods (push, pop, top, getMin) are $O(1)$ (required in the problem)
- SC: $O(2*n)$ -> $O(n)$ (stack + min_stack)

```python
from collections import deque

class MinStack:
    def __init__(self):
        self.stack = deque()
        self.min_stack = deque([2 ** 31]) # init w/ max val to handle inserting val when stack is empty


    # this implementation always maintain len(min_stack) == len(stack) + 1
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(self.min_stack[-1], val))


    def pop(self) -> None:
        assert bool(self.stack)

        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        assert bool(self.stack)

        return self.stack[-1]


    def getMin(self) -> int:
        assert bool(self.stack)

        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

```
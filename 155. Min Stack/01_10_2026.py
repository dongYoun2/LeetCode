# submission: https://leetcode.com/problems/min-stack/submissions/1881362135/
# runtime: 11 ms, memory: 22.40 MB

# 7 min
# refer to README.md or 10_06_2025.py for a complexity analysis.

# usual stack operations can be done in O(1) time. however, the problem here is to also return the minimum value in O(1) time. to achieve this, we can keep track of the minimum value in a separate stack every time we push a new value into the normal stack.


# cf.) the problem was straightforward now. maybe i struggled during previous attempts, especially 10/06/2025. 


from collections import deque

class MinStack:

    def __init__(self):
        self.normal_stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.normal_stack.append(val)
        if self.min_stack:
            curr_min = self.min_stack[-1]
            self.min_stack.append(min(curr_min, val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        assert self.normal_stack
        self.normal_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        assert self.normal_stack
        return self.normal_stack[-1]
        

    def getMin(self) -> int:
        assert self.normal_stack
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# notes while solving:
# normal_stack: 5 2 10 9 -100 1000
# min_stack: 5 2 2  2 -100 -100

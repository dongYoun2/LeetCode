# submission: https://leetcode.com/problems/min-stack/submissions/1604755340/

# 23 min
# TC: all methods (push, pop, top, getMin) are O(1) (required in the problem)
# SC: O(2*n) -> O(n) (stack + min_idx_stack)

# From LeetCode Top Interview 150 - Stack

# This is the second time solving this problem. The first time I solved this problem is on 2024-04-16.

# At first, I thought of keeping the one minimum index value but quickly realized that it would be problematic when popping the minimum value. So, I came up with the idea of keeping a list of minimum indices. When I was thinking without simulation, I thought there would be a case where the value in the middle of the minimum indices array has to be popped (this requires O(n) time complexity, which violates the problem requirements).

# However, after a simulation, I realized that it is not possible. The only case where the minimum index has to be popped is when the last element in the stack is the minimum value. Therefore, I found out that I could use a stack for the minimum indices as well.

# The LeetCode Editorial section shows that we could also keep the stack for "minimum values" themselves instead of the indices.

# Moreover, it is possible to implement all methods without any if-else conditions. For more details, refer to the markdown file.


from collections import deque


class MinStack:
    def __init__(self):
        self.stack = deque()
        self.min_idx_stack = deque()


    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.stack) == 1:
            assert len(self.min_idx_stack) == 0

            self.min_idx_stack.append(0)
        else:
            min_idx = self.min_idx_stack[-1]

            if self.stack[min_idx] > val:
                self.min_idx_stack.append(len(self.stack) - 1)


    def pop(self) -> None:
        assert len(self.stack) != 0

        if self.min_idx_stack[-1] == len(self.stack) - 1:
            self.min_idx_stack.pop()

        self.stack.pop()


    def top(self) -> int:
        assert len(self.stack) != 0
        return self.stack[-1]


    def getMin(self) -> int:
        assert len(self.stack) != 0
        return self.stack[self.min_idx_stack[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# notes while solving the problem:
# stack: 10 12 4
# min_indices: 0 2
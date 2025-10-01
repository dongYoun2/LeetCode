# submission: https://leetcode.com/problems/design-a-stack-with-increment-operation/submissions/1788207019/
# runtime: 38 ms, memory: 18.73 MB

# 5 min
# TC: O(1) for push, pop, and O(min(n, k) for increment, where n is the length of the stack and k is the number of elements to increment.
# SC: O(maxSize) for the stack


# Simple implementation problem using a stack.


from collections import deque

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = deque()
        self.max_cap = maxSize


    def push(self, x: int) -> None:
        if len(self.stack) < self.max_cap:
            self.stack.append(x)


    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()


    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

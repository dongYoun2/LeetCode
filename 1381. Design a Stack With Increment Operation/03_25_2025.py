# https://leetcode.com/problems/design-a-stack-with-increment-operation/

# 11 min
# TC: push - O(1), pop - O(1), increment - O(k)
# SC: O(maxSize)

from collections import deque

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = deque()
        self.max_len = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) >= self.max_len:
            return

        self.stack.append(x)


    def pop(self) -> int:
        try:
            return self.stack.pop()
        except IndexError:
            return -1


    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack), k)):
            self.stack[i] += val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

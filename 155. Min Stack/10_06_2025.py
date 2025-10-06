# submission: https://leetcode.com/problems/min-stack/submissions/1793284744/
# runtime: 9 ms, memory: 21.52 MB

# 33 min
# TC: O(1) for all methods (this is required in the problem)
# SC: O(2*n) -> O(n) (stack + min_stack)


# unlike when solving with 04_12_2025.py solution, i didn't know which data structure / algorithm to use in advance. so, since i have to implement all methods in O(1) time, i approached with using hash table to keep track of the minimum values in addition to the original stack.

# however, i realized that i only need to compare the minimum value so far with the new (or current) value, and if the former is smaller, then i just keep the previous min value, whereas if the latter is smaller, then i update the min value for the newly pushed value. therefore, the key is to add another stack that pushes the minimum value for each step. because of this, the length of both stacks should be the same.

# cf.) spent half an hour to figuring this out lol, but this is really elegant and simple! for the code even without if-else condition in push() method, refer to the markdown file.


from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()


    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            small = min(self.min_stack[-1], val)
            self.min_stack.append(small)


    def pop(self) -> None:
        assert self.stack
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        assert self.stack
        return self.stack[-1]


    def getMin(self) -> int:
        assert self.stack
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# notes while solving:
# -2 0 -3 -1

# 0 -2 -3

# -1


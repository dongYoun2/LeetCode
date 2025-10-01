# submission: https://leetcode.com/problems/design-a-stack-with-increment-operation/submissions/1788230721/
# runtime: 5 ms, memory: 19.00 MB
# this solution optimizes increment operation to O(1) time.

# 36 min (including first writing 09_30_2025.py code)
# TC: O(1) for push, pop, and increment
# SC: O(maxSize) for the stack


# the goal of this solution is to make the increment operation O(1) time. in the beginning, i was keep trying to mark the increment value in the separate hash table, but then eventually, hast table can grow up to O(n) space in the worst case, and have to scan through the entire hash table. after thinking for a while, i realized that i can mark the increment value in the stack itself, and "propagate" the increment value to the next stack top once we pop the stack. actually, i got the hint from note which i wrote that i can optimize the increment to O(1) time using "delayed propagation" after solving on 03/22/2025. i hope i can solve this without any hint next time.

# cf.) the reason this solution is absolutely valid is because stack API actually don't have the operation to scan through the entire stack. (for the peek operation, we can simply return self.stack[-1][0] + self.stack[-1][1], which is the sum of the 1) stack top value and the 2) increment value that needs to be applied to the stack top.)


from collections import deque

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = deque()
        self.max_cap = maxSize


    def push(self, x: int) -> None:
        if len(self.stack) < self.max_cap:
            self.stack.append([x, 0])   # val, inc_val


    def pop(self) -> int:
        if not self.stack:
            return -1

        val, inc_val = self.stack.pop()
        if self.stack:
            self.stack[-1][1] += inc_val    # propagating down to the next stack top inc_val
        return val + inc_val


    def increment(self, k: int, val: int) -> None:
        if not self.stack: return
        assert k >= 1 and self.stack

        pos = min(k, len(self.stack)) - 1
        self.stack[pos][1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
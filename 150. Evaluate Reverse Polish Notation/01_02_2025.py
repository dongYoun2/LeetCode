# submission: https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1872520961/
# runtime: 3 ms, memory: 19.18 MB

# 9 min
# TC: O(n), where n is the number of tokens
# SC: O(n) (stack)

# this is a typical stack problem. one caveat is that since 1) division always truncates towards zero and 2) there can be negative numbers, we need to use int(n1 / n2) instead of n1 // n2.

from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for tok in tokens:
            if tok == '+' or tok == '-' or tok == '*' or tok == '/':
                n2, n1 = stack.pop(), stack.pop()
                if tok == '+':
                    res = n1 + n2
                elif tok == '-':
                    res = n1 - n2
                elif tok == '*':
                    res = n1 * n2
                else:
                    res = int(n1 / n2)
                stack.append(res)
            else:
                stack.append(int(tok))

        assert len(stack) == 1
        return stack[0]

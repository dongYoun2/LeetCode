# problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# submission: https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1606778095/

# 17 min
# TC: O(n), where n is the number of tokens
# SC: O(n) (stack)

# From LeetCode Top Interview 150 - Stack

# Just one trivial thing to notice is that in the problem requirement, it says, "The division between two integers always truncates toward zero." So, in Python, we need to use int(n1 / n2) instead of n1 // n2 since `int()` truncates the decimal (rounding towards zero), whereas `//` performs integer (floor) division. They are the same when both n1 and n2 are positive, but they are different when one of them is negative. For example, -3 // 2 = -2, but int(-3 / 2) = -1.


from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                n2, n1 = stack.pop(), stack.pop()

                if token == "+":
                    n = n1 + n2
                    stack.append(n)
                elif token == "-":
                    n = n1 - n2
                    stack.append(n)
                elif token == "*":
                    n = n1 * n2
                    stack.append(n)
                elif token == "/":
                    n  = int(n1 / n2)
                    stack.append(n)

        return stack.pop()

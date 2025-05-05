# problem: https://leetcode.com/problems/valid-parentheses/
# submission: https://leetcode.com/problems/valid-parentheses/submissions/1625750664/

# 7 min
# TC: O(n), where n is the length of the string
# SC: O(n)

# From LeetCode Top Interview 150 - Stack

# Typical stack problem. I had solved this problem before on 03/27/2025, and this is the second time solving it.


from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            try:
                if c == "(" or c == "{" or c == "[":
                    stack.append(c)
                elif c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            except IndexError:  # no opening bracket for the closing bracket
                return False

        return len(stack) == 0

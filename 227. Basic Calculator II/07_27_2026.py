# submission: https://leetcode.com/problems/basic-calculator-ii/submissions/2083753105/
# runtime: 119 ms (beats 7.54%), memory: 24.72 MB (beats 8.03%)
# 53 min
# solved using stack

# TC: O(n), where n is the length of the input string
# SC: O(n)


# took longer than expected. there were two points that i forgot to consider and thought wrong about so that i submit wrong implementations:
# 1. we need to be aware when processing numbers in a string that one integer can be multiple digits
# 2. when computing the '+' and '-', the order should be a normal left to right order, not a stack based order

# however, below code is hard to read and quite messy. also the runtime is slow. for a better solution, refer to the READMe.md.


from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        
        # find the first number
        i = 0
        n_str = []
        while i < len(s) and s[i].isnumeric():
            n_str.append(s[i])
            i += 1
        stack = deque([int("".join(n_str))])

        # process all characters while computing intermediate results for '*' and '/'
        while i < len(s):
            if s[i].isnumeric():
                n2_str = [s[i]]
                while i+1 < len(s) and s[i+1].isnumeric():
                    n2_str.append(s[i+1])
                    i += 1
                n2 = int("".join(n2_str))

                if stack[-1] == '*' or stack[-1] == '/':
                    op, n1 = stack.pop(), stack.pop()
                    res = n1 * n2 if op == '*' else n1 // n2

                    stack.append(res)
                else:
                    stack.append(n2)
            else:
                stack.append(s[i])
            i+= 1

        # compute '+' and '-' after processing all characters
        arr = list(stack)
        ans = arr[0]
        if len(arr) > 1:
            op = None
            for i in range(1, len(arr)):
                if isinstance(arr[i], int):
                    ans = ans + arr[i] if op == '+' else ans - arr[i]
                else:
                    op = arr[i]


        return ans

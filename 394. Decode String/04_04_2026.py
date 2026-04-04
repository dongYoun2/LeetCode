# submission: https://leetcode.com/problems/decode-string/submissions/1968958025/
# runtime: 0 ms (beats 100.00%), memory: 19.40 MB (beats 57.46%)
# 20 min

# TC: O(n), where n is the length of the input string
# SC: O(n) (output space is not counted)


# after several simulations, i realized this is a stack problem. one important edge case is that 'k' can be a multi-digit number; so we need to parse the number properly. another caveat is that when checking with `tack[-1].isnumeric()`, there can be a case where the stack is empty; and  because of this, default `k` should be 1. last thing to be aware of is that we need to reverse both the characters in the current string and the digits of the number.

# the implementation below is acceptable, but it's a little verbose. for cleaner and concise code, refer to this submission: https://leetcode.com/problems/decode-string/submissions/1968971823/ — runtime: 0 ms (beats 100.00%), memory: 19.28 MB (beats 85.73%)


from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        
        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            curr = []
            while True:
                top = stack.pop()
                
                if top != '[':
                    curr.append(top)
                else:
                    k_digits = []
                    while stack and stack[-1].isnumeric():
                        d = stack.pop()
                        k_digits.append(d)
                    
                    k = int("".join(reversed(k_digits))) if k_digits else 1

                    curr_s = "".join(reversed(curr)) * k
                    stack.append(curr_s)
                    break

        return "".join(stack)

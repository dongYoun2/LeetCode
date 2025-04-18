# problem: https://leetcode.com/problems/two-sum/
# submission: https://leetcode.com/problems/basic-calculator/submissions/1610467217/

# TC: O(n), where n is the length of the string
# SC: O(n) (for stack)

# From LeetCode Top Interview 150 - Stack

# A stack is typically used for a simple calculator implementation.

# It took so long to solve this problem. There are two points that I forgot to consider at first:
# 1. There are no multiplication or division operations in the string.
# 2. A string such as "4123" should be converted to 4123.

# So, my initial approach was to construct the expression tree from the given infix expression. Then, traverse the tree to get the postfix expression, and compute the result using a stack. However, I failed to construct the tree.

# This approach is valid, but the tree is unnecessary here. Postfix notation can be directly converted from infix notation. Also, even converting to postfix notation is unnecessary for this problem since the expression is simple; i.e., no multiplication or division.

# After realizing the tree is not needed for this problem, I started to think about directly converting the infix to a postfix using a stack. As I still thought multiplication and division could exist in the expression, I needed to consider operator precedence. Again, after realizing that's not the case, so that I don't even need to convert to a postfix notation, I then started thinking about how to handle the minus unary operation. This can be addressed by keeping the `is_addition` flag in the code below with the initial number 0 (`ans` = 0).

# Finally, as I forgot to consider the second point above, I got an error on the input where the string is "2147483647". Thus, I used regex to tokenize the string.

# The code below solves all the subexpressions once it encounters the closing parenthesis. This is a bit different from the typical stack implementation, where the subexpression is computed on the fly (LeetCode Editorial Approach 2: Stack and No String Reversal). For more details, refer to the Editorial section or this solution code from another user: https://leetcode.com/problems/basic-calculator/solutions/546092/simple-python-solution-using-stack-with-explanation-inline/.


# cf.) I started attempting this problem at night on 04/17/2025, spending, I think, more than an hour and a half. After failing on the input "2147483647", I was done with my brain energy for the day. So, I fixed it with a fresh mind on 04/18/2025 in the morning, tokenizing the string with a regular expression.



from collections import deque
import re

class Solution:
    def calculate(self, s: str) -> int:
        def calc_subexpression(arr):
            reversed_arr = arr[::-1]

            ans = 0
            is_addition = True
            for e in reversed_arr:
                if isinstance(e, int):
                    if is_addition:
                        ans += e
                    else:
                        ans -= e
                elif e == "+":
                    is_addition = True
                else:
                    is_addition = False

            return ans


        s = s.strip().replace(" ", "")
        s = "(" + s + ")"

        parts = re.split(r"([\+\-\(\)])", s)
        parts = [p for p in parts if p != ""]

        stack = deque()

        for part in parts:
            sub_exp_arr = []
            if part != ")":
                if part.isdigit():
                    part = int(part)
                stack.append(part)
            else:
                popped = stack.pop()
                while popped != "(":
                    sub_exp_arr.append(popped)
                    popped = stack.pop()

                sub_num = calc_subexpression(sub_exp_arr)
                stack.append(sub_num)

        assert len(stack) == 1
        return stack[0]

[Problem](https://leetcode.com/problems/basic-calculator-ii/description/)


## Stack-based Solution

The insight is that the stack stores terms that are already ready to be added instead of storing numbers and operators. So, for a stack problem, good question to ask is "Can I encode information so that the final computation becomes trivial?"


[Submission](https://leetcode.com/problems/basic-calculator-ii/submissions/2083837070/)—Runtime: 34 ms (beats 98.16%), Memory: 22.61 MB (beats 15.84%)

TC: $O(n)$, where $n$ is the length of the input string
SC: $O(n)$


```python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"

        for char in s + "+":  # Sentinel processes the final number
            if char.isdigit():
                num = num * 10 + int(char)

            elif char in "+-*/":
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:
                    prev = stack.pop()
                    # Python '//' floors for negatives; emulate truncation toward zero.
                    result = abs(prev) // num
                    stack.append(result if prev >= 0 else -result)

                op = char
                num = 0

        return sum(stack)

```
# submission: https://leetcode.com/problems/add-binary/submissions/1667781248/
# runtime: 3 ms, memory: 17.7 MB

# 11 min
# TC: O(max(m, n)), where m is the length of `a` and n is the length of `b`.
# SC: O(max(m, n)), for keeping `answer` array.


# From LeetCode Top Interview 150 - Bit Manipulation

# This is indeed not a bit manipulation solution. Rather, it is a simulation of the addition process (or a simple implementation of the AC).

# The code below can be improved in two ways:
# 1. We can simply use `//` and `%` operators (or `divmod` function) to find a proper digit and carry instead of using if-else statements. `s % 2` gives us the digit to append, and `s // 2` gives us the carry for the next iteration.
# 2. We can also use Python string's `zfill()` function to pad the shorter string with leading zeros instead of manually calculating the difference in lengths and prepending zeros.

# Bit manipulation solution can be found in the Editorial section's Approach 2 or the markdown file.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a

        assert len(a) == len(b)

        answer = []
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            a_digit, b_digit = int(a[i]), int(b[i])

            s = a_digit + b_digit + carry

            if s == 0:
                answer.append(0)
                carry = 0
            elif s == 1:
                answer.append(1)
                carry = 0
            elif s == 2:
                answer.append(0)
                carry = 1
            elif s == 3:
                answer.append(1)
                carry = 1

        if carry == 1:
            answer.append(carry)

        answer.reverse()

        return "".join([str(n) for n in answer])

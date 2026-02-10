# submission: https://leetcode.com/problems/string-to-integer-atoi/submissions/1913935463/
# runtime: 0 ms (Beats 100.00%), memory: 19.3 MB (Beats 49.44%)
# 25 min


# though the submission is correct, the code below is technically wrong because:
# 1. int() function is used
# 2. the work is still be done even after the clamp is reached (this works here becasue python integers are unbounded)

# the purpose of the problem is to clamp 32-bit range to match other languages, such as C and C++, behavior. moreover, better way to handle the sign is to convert to the corresponding sign at the end.

# for a correct impelementation, refer to the README file.


class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        is_positive = True
        in_leading = True
        for c in s:
            if in_leading and c == " ":
                continue
            elif in_leading and c == "+":
                in_leading = False
            elif in_leading and c == "-":
                in_leading = False
                is_positive = False
            elif '0' <= c <= '9':
                in_leading = False
                ans *= 10
                ans += int(c) if is_positive else -int(c)

                if ans > 2**31-1:
                    ans = 2**31 - 1
                elif ans < -2**31:
                    ans = -2**31
            else:
                break
        
        return ans

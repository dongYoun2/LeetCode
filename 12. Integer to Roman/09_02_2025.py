# submission: https://leetcode.com/problems/integer-to-roman/submissions/1757165742/
# runtime: 7 ms, memory: 17.8 MB

# 28 min
# TC: O(1), since the number of digits is limited to 4 (input size is fixed)
# SC: O(1)


# this is the second time solving this problem. first time was on 03/17/2025, which took around 45 min to solve (https://leetcode.com/problems/integer-to-roman/submissions/1577232564/).

# the code below is legit, but there's simpler and more readable solution. instead of iterating through the divisor (1000 -> 100 -> 10 -> 1), which is driven by the place value (digits) of the input number, we can iterate through the predefined sorted list of (value, roman symbol) pairs (in my case, the sorted `mapping` dictionary). this insight is driven by the symbols rather than the number's digit structure.

# KEY TAKEAWAY: iterating through a predefined sorted list of (value, symbol) pairs (including subtractive cases) is cleaner as it makes the rules explicit and the loop logic uniform. (for more details refer to the Editorial's Approach 1.)


class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }

        divisor = 1000

        ans = ""
        while divisor >= 1:
            q, num = divmod(num, divisor)

            decimal_val = divisor * q

            if decimal_val in mapping:
                roman_char = mapping[divisor * q]
            elif q == 4 or q == 9:
                a = 1 * divisor
                b = (q + 1) * divisor
                roman_char = mapping[a] + mapping[b]
            elif q > 5:
                roman_char = mapping[divisor * 5] + mapping[divisor] * (q - 5)
            elif q != 0:
                roman_char = mapping[divisor] * q
            else:
                roman_char = ''

            ans += roman_char
            divisor //= 10

        return ans

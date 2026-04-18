# submission: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/submissions/1981792567/
# Time Limit Exceeded
# spent aorund 46 min

# TC: O(n^2)
# Sc: (1)


# chose from the "sliding window" category.

# after submitting, "04_18_2026_wrong.py" code, i looked at two hints in the problem appendix, but those were what i already keeping aware of. so i simply implemented the brute force solution that i thought of before, and submitted it. expected to get TLE.

# then i spent an additional 9 min (so totla 55 min on this problem), to come up with the correct sliding window solution, but could not. i asked chatgpt, and was mind-blown by the trick to double the string.


import math

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        def check(b_string):
            starts_one = 0
            for i in range(n):
                if i % 2 == 0 and b_string[i] == '0':
                    starts_one += 1
                if i % 2 == 1 and b_string[i] == '1':
                    starts_one += 1
            starts_zero = 0
            for i in range(n):
                if i % 2 == 0 and b_string[i] == '1':
                    starts_zero += 1
                if i % 2 == 1 and b_string[i] == '0':
                    starts_zero += 1
            
            return min(starts_one, starts_zero)


        ans = math.inf
        for i in range(n):
            ans = min(ans, check(s[i:] + s[:i]))
        
        return ans

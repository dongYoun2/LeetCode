# submission: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/submissions/1981778896/
# wrong answer
# spent around 28 min

# chose from the "sliding window" category.

# though i chose from the sliding window category, i cannot directly think of how to use the sliding window technique. so, i tried simulating and came up with the brute force solution, where we try all possible rotations and compare with the two patterns (010101... and 101010...) for each rotation. 

# however, idk why, but somehow i thought for the odd length strings, it's enough to test for the original string and the string with one rotation, and for the even length strings, only for the original string. but this is so obvious that it's wrong; for the simple even-length counterexample, s = "110011", the string for the correct answer is "011110", where 3 rotations are needed (not 0 rotations).

# want to justify that i was so tired today in the morning, lol.


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
        ans = min(ans, check(s))

        if n % 2 == 1:
            new_s = s[1:] + s[0]
            ans = min(ans, check(new_s))
        
        return ans

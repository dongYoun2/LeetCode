# problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# submission: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1636861581/?envType=study-plan-v2&envId=top-interview-150

# 15 min
# TC: O(4^n), where n (0 <= n <= 4) is the length of `digits`. (The constant 4 is the maximum number of letters for a digit.)
# SC: O(1) (Output space doesn't count.)

# From LeetCode Top Interview 150 - Backtracking

# This is a brute-force solution using nested loops. It uses dummy (or padding) digits to make the number of digits 4, since the maximum number of digits is 4 in the problem constraint. It can be further generalized by initializing the `ans` list with the single empty prefix, that is `ans = [""]`.


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        digit_map = {
            '1': ['$'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        n = n_temp = len(digits)
        digits_temp = digits

        while n_temp < 4:
            digits_temp += '1'
            n_temp += 1

        ans = []
        for a in digit_map[digits_temp[0]]:
            for b in digit_map[digits_temp[1]]:
                for c in digit_map[digits_temp[2]]:
                    for d in digit_map[digits_temp[3]]:
                        ans.append(a + b + c + d)

        ans = [e[:n] for e in ans]

        return ans

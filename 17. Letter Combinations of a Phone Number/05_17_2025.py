# submission: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1636870539/
# runtime: 0 ms, memory: 17.73 MB

# 7 min
# TC: O(n*4^n), where n (0 <= n <= 4) is the length of `digits`. First O(n) is for the join operation. (The constant 4 is the maximum number of letters for a digit.)
# SC: O(n) (each for the `l` list and the extra space interally used in `product()`. Output space doesn't count.)

# From LeetCode Top Interview 150 - Backtracking

# This is a brute-force solution using `itertools.product()`. Since the number of digits is at most 4, we can simply use a brute-force solution to generate all combinations of letters for the given digits.

# cf.) If the number of digits is large, we can use DFS backtracking with pruning. It's important to note that backtracking shines only when we can prune the search space.


from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        digit_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        l = [digit_map[d] for d in digits]
        combs = product(*l)

        return ["".join(e) for e in combs]

# submission: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1636888019/
# runtime: 3 ms, memory: 17.82 MB

# 11 min
# TC: O(4^n), where n (0 <= n <= 4) is the length of `digits`. (The constant 4 is the maximum number of letters for a digit.)
# SC: O(1) (output space doesn't count.)

# From LeetCode Top Interview 150 - Backtracking

# Below is a BFS solution.


from collections import deque

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

        q = deque(digit_map[digits[0]]) # in the end, queue is the answer output

        for i in range(1, len(digits)):
            for _ in range(len(q)):
                comb = q.popleft()
                for c in digit_map[digits[i]]:
                    q.append(comb + c)

        return list(q)

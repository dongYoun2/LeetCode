# submission: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1928971383/
# runtime: 0 ms (beats 100.00%), memory: 19.56 MB (beats 8.45%)
# 10 min

# refer to the 05_17_2025_dfs_backtrack.py for the time and space complexity analysis.


# though i knew i could solve usig the python itertools module, i solved it with a dfs backtracking approach since i believe this would be the purpose of this problem.

# unlike 05_17_2025_dfs_backtrack.py and 10_24_2025.py, i built the final answer string in the end at once using string 'join' method instead of building it incrementally. this way is better since python strings are immutable.

# another improvement that could be made is using string for the `d_to_chars` dictionary value instead of a list because we are simply iterating over the characters, not modifying them. iterating over a string is more efficient.


from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d_to_chars = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        ans = []


        def dfs(d_idx: int, curr: List[str]):
            if d_idx >= len(digits):
                ans.append(''.join(curr))
                return

            chars = d_to_chars[digits[d_idx]]
            for c in chars:
                curr.append(c)
                dfs(d_idx+1, curr)
                curr.pop()

        
        dfs(0, [])
        return ans

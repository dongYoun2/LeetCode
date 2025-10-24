# submission: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1810555731/
# runtime: 0 ms, memory: 17.81 MB

# 9 min
# refer to the 05_17_2025_dfs_backtrack.py for the time and space complexity analysis.


# i remeber this is a backtracking problem from the figure shown in the problem description lol. it was pretty straightforward to implement. note that backtracking shines when we can prune the search space, though we cannot prune anything for this problem.

# for more details, refer to the 10_24_2025_dfs_backtrack.py.


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_ch = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        ans = []
        def dfs(i: int, curr: str):
            if i >= len(digits):
                ans.append(curr)
                return

            n = digits[i]
            for ch in digit_to_ch[int(n)]:
                dfs(i + 1, curr + ch)


        dfs(0, '')
        return ans

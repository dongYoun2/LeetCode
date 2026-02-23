# submission: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1636928913/
# runtime: 0 ms, memory: 17.67 MB
# 23 min

# TC: O(4*n), where n (0 <= n <= 4) is the length of `digits`. (The constant 4 is the maximum number of letters for a digit.)
# SC: O(n) (for the recursion stack space, which is the maximum depth of the recursion tree.)

# From LeetCode Top Interview 150 - Backtracking

# Although I knew this was a backtracking problem, I simply implemented it using the brute-force approach with `itertools.product()` at first (05_17_2025.py) since I couldn't think of a direct backtracking solution. It took me a bit of time to implement the backtracking solution properly. It's good to notice that backtracking mostly comes with the DFS approach, and it shines when we can prune the search space (however, we cannot prune anything for this problem).

# Backtracking generally follows the steps below:
# 1. "Choose" a candidate from the current position.
# 2. "Explore" the next position.
# 3. "Un-choose" the candidate (backtrack) and go to the next candidate.

# These correspond to the following in the code below:
# 1. Choose a letter c for the current digit.
# 2. Explore by recursing on the tail of the string with `comb_string + c`.
# 3. Un-choose happens implicitly when that recursive call returns (since we never mutate `comb_string` in place). (The Editorial section explicitly uses `pop()` since it modifies the list (containing the current combination) in place.)

# Additionally, the code below can be further optimized to prevent creating new strings for each recursive call by:
# 1. Passing the index of the current digit instead of slicing the `digits` string.
# 2. Using a list to store the current combination instead of a string.
# The Editorial section shows this optimized version. Refer to it for the code itself.


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

        def dfs_backtrack(digits, comb_string):
            if len(digits) == 0:
                ans.append(comb_string)
                return

            first_digit = digits[0]
            for c in digit_map[first_digit]:
                dfs_backtrack(digits[1:], comb_string + c)


        ans = []
        dfs_backtrack(digits, "")

        return ans
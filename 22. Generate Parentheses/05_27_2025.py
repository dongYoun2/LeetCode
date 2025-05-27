# submission: https://leetcode.com/problems/generate-parentheses/submissions/1646134677/

# 17 min

# TC: O(2^{2n} / n^{1/2}) -> O(4^n / n^{1/2}), where n is the number of pairs of parentheses.
# - The n-th Catalan number (C_n) (the number of valid parentheses strings of length 2n) is C_n \;=\;\frac{1}{n+1}\binom{2n}{n}\;\approx\;\frac{4^n}{n^{3/2}\sqrt{\pi}}. The number of solutions is exactly the C_n of them, and for each solution, we write down a complete string (O(n)). Hence, the final time complexity is O(C_n * n) = O(4^n / n^{1/2} * n) = O(4^n / n^{1/2}).
# -> To analyze the time complexity in practice, we can simply reason that it would take O(2^{2n}) time to generate all possible combinations of parentheses (plain-vanilla backtracking). This works in this problem since the maximum value of n is 8, which means the maximum number of combinations is 2^16 = 65536, which is manageable.

# SC: O(n^2). (n for the recursion stack and n for the string concatenation for each backtrack call)
# - The below code backtracks implicitly by using the string concatenation, which is O(n) for each backtrack call. This can be improved to O(1) by using a list and mutating it in place (explicit backtracking), leading to an overall space complexity of O(n).


# From LeetCode Top Interview 150 - Backtracking

# I used a backtracking algorithm to generate valid parentheses combinations. The core idea in backtracking is to prune the search space. Here, this is done by ensuring that the number of closing parentheses never exceeds the number of opening parentheses at any point in the string. Moreover, whenever the number of opening parentheses reaches n, we append the remaining closing parentheses to the string, as they are guaranteed to be valid. In short, backtracking is simply pruning the search space from the brute-force approach.

# cf.) The brute-force approach also works here since the maximum value of n is 8. Additionally, divide and conquer approavch can also be used. For more details, refer to the Editorial section.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(paran, open_paran_cnt, close_paran_cnt):
            if close_paran_cnt > open_paran_cnt:
                return

            if len(paran) == 2*n:
                ans.append(paran)
                return

            if open_paran_cnt == n:
                backtrack(paran + ")" * (n - close_paran_cnt), n, n)
            else:
                backtrack(paran + "(", open_paran_cnt + 1, close_paran_cnt)
                backtrack(paran + ")", open_paran_cnt, close_paran_cnt + 1)


        ans = []
        backtrack("", 0, 0)

        return ans

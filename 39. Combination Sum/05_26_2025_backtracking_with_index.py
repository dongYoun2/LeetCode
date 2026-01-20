# submission: https://leetcode.com/problems/combination-sum/submissions/1645531762/
# runtime: 6 ms, memory: 17.9 MB

# 15 min (time coding up 05_26_2025.py included)
# refer to the README.md for the complexity analysis. though the asymptotic time complexity is the same as the README solution (pruned version), the runtime is slower compared to the README solution in practice.


# From LeetCode Top Interview 150 - Backtracking


# The runtime is significantly improved compared to the "05_26_2025.py" by using the cursor index (`start`) to indicate the loop's starting index instead of sorting, tuple, set, and list conversion.

# However, this can be further optimized by pruning the search space by skipping candidates greater than the remaining target. To do this, we first need to sort candidates. For more details, refer to the README.md.


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(curr, start, remain):
            if remain == 0:
                ans.append(curr[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                dfs(curr, i, remain - candidates[i])
                curr.pop()

        ans = []
        dfs([], 0, target)

        return ans
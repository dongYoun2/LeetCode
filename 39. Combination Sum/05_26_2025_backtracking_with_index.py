# submission: https://leetcode.com/problems/combination-sum/submissions/1645531762/

# 15 min (time coding up 05_26_2025.py included)
# runtime: 6 ms, memory: 17.9 MB
# TC: O(n^d), where n is the number of candidates and d is the maximum depth of the recursion (d \approx target / min(candidates)).
# - O(n^d): Total number of calls in the DFS tree; at each node, we loop over all n candidates, and we can go as deep as d.
# -> So the overall time complexity is exponential in "target".
# SC: O(2*d) -> O(d) (O(d) for the recursion stack and current combination storage respectively)


# From LeetCode Top Interview 150 - Backtracking


# The runtime is significantly improved by using the cursor index (`start`) to indicate the loop's starting index instead of sorting, tuple, set, and list conversion.

# However, this can be further optimized by pruning the search space by skipping candidates greater than the remaining target. To do this, we first need to sort candidates. For more details, refer to the markdown file.


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
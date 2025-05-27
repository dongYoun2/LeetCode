# submission: https://leetcode.com/problems/combination-sum/submissions/1645531539/

# 11 min
# runtime: 412 ms, memory: 18 MB
# TC: O(n^d * d log d), where n is the number of candidates and d is the maximum depth of the recursion (d \approx target / min(candidates)).
# - O(n^d): Total number of calls in the DFS tree; at each node, we loop over all n candidates, and we can go as deep as d.
# - O(d log d): At each "solution" leaf node, we sort the current combination of candidates, which takes O(d log d) time.
# -> So the overall time complexity is exponential in "target".
# SC: O(2*d) -> O(d) (O(d) for the recursion stack and current combination storage respectively)


# From LeetCode Top Interview 150 - Backtracking

# After implementing the solution with a backtracking algorithm, the problem was that the same combination would be counted multiple times—e.g., [2,2,3] and [2,3,2] would be counted as different combinations. I used sorting, a tuple, and a set to prevent this issue. However, this approach is not optimal, as it sorts the current combination at each leaf node, which can be costly. Instead of sorting solution candidates every time, I realized that the duplicates can also be avoided by passing the current cursor index to the recursive function, which is a more efficient way. This approach is in "05_26_2025_backtracking_with_index.py".



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(curr, remain):
            if remain == 0:
                ans.add(tuple(sorted(curr[:])))
                return

            if remain < 0:
                return

            for candidate in candidates:
                curr.append(candidate)
                dfs(curr, remain - candidate)
                curr.pop()


        ans = set()
        dfs([], target)

        return list(ans)